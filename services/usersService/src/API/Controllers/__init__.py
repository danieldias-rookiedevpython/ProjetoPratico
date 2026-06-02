from .AdminController import routerAdmins
from .AtendentController import routerAtendents
from .MedicController import routerMedics, routerUsers
from .PacientController import routerPacients

__all__ = ["routerAdmins", "routerAtendents", "routerMedics", "routerPacients", "routerUsers"]
