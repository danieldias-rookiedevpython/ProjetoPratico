from services.usersService.src.infra.adapters.EventBus import InMemoryEventBus
from services.usersService.src.infra.adapters.RoleScopedUserRepository import RoleScopedUserRepository
from services.usersService.src.modules.pacients.application.useCases.CreateUseCase import CreatePacientUseCase
from services.usersService.src.modules.pacients.application.useCases.DeleteUseCase import DeletePacientUseCase
from services.usersService.src.modules.pacients.application.useCases.DetailUseCase import DetailPacientUseCase
from services.usersService.src.modules.pacients.application.useCases.ListUseCase import ListPacientUseCase
from services.usersService.src.modules.pacients.application.useCases.UpdateUseCase import UpdatePacientUseCase
from services.usersService.src.modules.users.application.useCases.commands.admin.CreateUseCase import CreateAdminUseCase
from services.usersService.src.modules.users.application.useCases.commands.admin.DeleteUseCase import DeleteAdminUseCase
from services.usersService.src.modules.users.application.useCases.commands.admin.UpdateUseCase import UpdateAdminUseCase
from services.usersService.src.modules.users.application.useCases.commands.atendent.CreateUseCase import CreateAtendentUseCase
from services.usersService.src.modules.users.application.useCases.commands.atendent.DeleteUseCase import DeleteAtendentUseCase
from services.usersService.src.modules.users.application.useCases.commands.atendent.UpdateUseCase import UpdateAtendentUseCase
from services.usersService.src.modules.users.application.useCases.commands.medic.CreateUseCase import CreateMedicUseCase
from services.usersService.src.modules.users.application.useCases.commands.medic.DeleteUseCase import DeleteMedicUseCase
from services.usersService.src.modules.users.application.useCases.commands.medic.UpdateUseCase import UpdateMedicUseCase
from services.usersService.src.modules.users.application.useCases.querys.admin.DetailUseCase import DetailAdminUseCase
from services.usersService.src.modules.users.application.useCases.querys.admin.ListUseCase import ListAdminUseCase
from services.usersService.src.modules.users.application.useCases.querys.atendent.DetailUseCase import DetailAtendentUseCase
from services.usersService.src.modules.users.application.useCases.querys.atendent.ListUseCase import ListAtendentUseCase
from services.usersService.src.modules.users.application.useCases.querys.medic.DetailUseCase import DetailMedicUseCase
from services.usersService.src.modules.users.application.useCases.querys.medic.ListUseCase import ListMedicUseCase


class UserFactory:
    @staticmethod
    def event_bus_factory():
        return InMemoryEventBus()

    @staticmethod
    def medic_repository_factory():
        return RoleScopedUserRepository("MEDICO")

    @staticmethod
    def atendent_repository_factory():
        return RoleScopedUserRepository("ATENDENTE")

    @staticmethod
    def admin_repository_factory():
        return RoleScopedUserRepository("ADMIN")

    @staticmethod
    def pacient_repository_factory():
        return RoleScopedUserRepository("PACIENTE")

    @staticmethod
    def create_medic_use_case():
        return CreateMedicUseCase(UserFactory.medic_repository_factory(), UserFactory.event_bus_factory())

    @staticmethod
    def update_medic_use_case():
        return UpdateMedicUseCase(UserFactory.medic_repository_factory(), UserFactory.event_bus_factory())

    @staticmethod
    def delete_medic_use_case():
        return DeleteMedicUseCase(UserFactory.medic_repository_factory(), UserFactory.event_bus_factory())

    @staticmethod
    def list_medic_use_case():
        return ListMedicUseCase(UserFactory.medic_repository_factory())

    @staticmethod
    def detail_medic_use_case():
        return DetailMedicUseCase(UserFactory.medic_repository_factory())

    @staticmethod
    def create_atendent_use_case():
        return CreateAtendentUseCase(UserFactory.atendent_repository_factory(), UserFactory.event_bus_factory())

    @staticmethod
    def update_atendent_use_case():
        return UpdateAtendentUseCase(UserFactory.atendent_repository_factory(), UserFactory.event_bus_factory())

    @staticmethod
    def delete_atendent_use_case():
        return DeleteAtendentUseCase(UserFactory.atendent_repository_factory(), UserFactory.event_bus_factory())

    @staticmethod
    def list_atendent_use_case():
        return ListAtendentUseCase(UserFactory.atendent_repository_factory())

    @staticmethod
    def detail_atendent_use_case():
        return DetailAtendentUseCase(UserFactory.atendent_repository_factory())

    @staticmethod
    def create_admin_use_case():
        return CreateAdminUseCase(UserFactory.admin_repository_factory(), UserFactory.event_bus_factory())

    @staticmethod
    def update_admin_use_case():
        return UpdateAdminUseCase(UserFactory.admin_repository_factory(), UserFactory.event_bus_factory())

    @staticmethod
    def delete_admin_use_case():
        return DeleteAdminUseCase(UserFactory.admin_repository_factory(), UserFactory.event_bus_factory())

    @staticmethod
    def list_admin_use_case():
        return ListAdminUseCase(UserFactory.admin_repository_factory())

    @staticmethod
    def detail_admin_use_case():
        return DetailAdminUseCase(UserFactory.admin_repository_factory())

    @staticmethod
    def create_pacient_use_case():
        return CreatePacientUseCase(UserFactory.pacient_repository_factory(), UserFactory.event_bus_factory())

    @staticmethod
    def update_pacient_use_case():
        return UpdatePacientUseCase(UserFactory.pacient_repository_factory(), UserFactory.event_bus_factory())

    @staticmethod
    def delete_pacient_use_case():
        return DeletePacientUseCase(UserFactory.pacient_repository_factory(), UserFactory.event_bus_factory())

    @staticmethod
    def list_pacient_use_case():
        return ListPacientUseCase(UserFactory.pacient_repository_factory())

    @staticmethod
    def detail_pacient_use_case():
        return DetailPacientUseCase(UserFactory.pacient_repository_factory())

    useCaseCreateUser_factory = create_medic_use_case
    useCaseDeleteUser_factory = delete_medic_use_case
    useCaseUpdateUser_factory = update_medic_use_case
    useCaseListUser_factory = list_medic_use_case
    useCaseDetailUser_factory = detail_medic_use_case
