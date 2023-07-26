from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from reservation.models import Reservation 


 # Fonction pour modifier les statuts des voiture réserver et le statut d'une réservation

def update_car_statuses():
    reservations = Reservation.objects.all()
    date_du_jour = timezone.now().date() 

    for reservation in reservations:
        if reservation.dateReservation == date_du_jour :
            reservation.voiture.statutVoiture= True
        reservation.voiture.save()

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_car_statuses, 'interval', days=1)  
    scheduler.start()
