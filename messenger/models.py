from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']


class ThreadManager(models.Manager):
    def find(self, user1, user2):
        queryset = self.filter(users=user1).filter(users=user2)
        if len(queryset) > 0:
            return queryset[0]
        return None
    
    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread


class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
    updated = models.DateTimeField(auto_now=True)

    objects = ThreadManager()
    
    class Meta:
        ordering = ['-updated']


# signal
def messages_changed(sender, **kwargs):
    instance = kwargs.pop("instance", None)
    action = kwargs.pop("action", None)
    pk_set = kwargs.pop("pk_set", None)
    print(instance, action, pk_set)
    
    false_pk_set = set()
    
    # Busca los mensajes que existen a partir de la clave primaria pk_set
    # y si el usuario que los ha creado no forma parte del hilo que existe en 
    # instance, lo borra para que no se añadan.
    # Intercepta el mensaje antes de que se añada
    if action is "pre_add":
        # recorre todos los mensajes que hay en el pk_set
        for msg_pk in pk_set:
            # recupera los mensajes
            msg = Message.objects.get(pk=msg_pk)
            # para cada mensaje se comprueba: si el autor del mensaje no se
            # encuentra dentro de los usuarios que hay añadidos en la instancia del hilo
            if msg.user not in instance.users.all():
                # muestra un debug
                print("Ups, ({}) no forma parte del hilo".format(msg.user))
                # almacena los mensajes no permitidos
                false_pk_set.add(msg_pk)
                
    # busca los mensajes de false_pk_set que si están en pk_set y los borra de pk_set
    pk_set.difference_update(false_pk_set)
    
    # fuerza la actualización haciendo un save()
    instance.save()
                
# conecta la señal a cualquier cambio que suceda en el campo 'messages' de Thread
m2m_changed.connect(messages_changed, sender=Thread.messages.through)