# Endpoints e Gateway

Esta documentacao lista os endpoints expostos pelos servicos da aplicacao e como eles devem ser acessados pelo Traefik.

Base local do gateway:

```text
http://localhost
```

## Gateway Traefik

| Servico | Prefixo publico | Servico Docker | Porta interna | Middleware |
| --- | --- | --- | --- | --- |
| Auth | `/auth` | `auth-service` | `8000` | publico |
| Users | `/users` | `users-service` | `8000` | `auth@file`, strip `/users` |
| Agenda | `/agenda` | `agenda-service` | `8000` | `auth@file` |
| Notification | `/notification` | `notificacao-service` | `8000` | `auth@file`, strip `/notification` |
| Analytics | `/analytics` | `analytic-service` | `8000` | `auth@file` |

Rotas protegidas devem receber:

```text
Authorization: Bearer <token>
```

O middleware `auth@file` chama `http://auth-service:8000/auth/validate` e repassa os headers `X-User-Id` e `X-User-Role`.

## Autorizacao OpenFGA

O OpenFGA e inicializado automaticamente pelo servico `openfga-init` definido no `docker-compose.yml` da raiz. Ao subir a aplicacao, ele:

1. espera o OpenFGA responder;
2. cria ou reutiliza a store `agendamento-medico`;
3. publica o modelo de autorizacao de `openfga/authorization-model.json`;
4. grava as permissoes iniciais de `openfga/tuples.json`.

O fluxo de autorizacao fica centralizado no `auth-service`:

1. o Traefik recebe a request;
2. para rotas protegidas, chama `/auth/validate`;
3. o auth valida o JWT;
4. o auth consulta o OpenFGA usando o usuario, o cargo/role e o servico acessado;
5. se o OpenFGA permitir, a request segue para o servico final.

Mapeamento padrao:

| Metodo HTTP | Relacao OpenFGA |
| --- | --- |
| `GET`, `HEAD`, `OPTIONS` | `can_read` |
| `POST`, `PUT`, `PATCH`, `DELETE` | `can_write` |

Objetos protegidos:

| Prefixo | Objeto OpenFGA |
| --- | --- |
| `/users` | `service:users` |
| `/agenda` | `service:agenda` |
| `/notification` | `service:notification` |
| `/analytics` | `service:analytics` |

As regras iniciais ficam em `openfga/tuples.json`. Para alterar permissoes padrao, edite esse arquivo e suba novamente a stack.

## Auth Service

Prefixo publico: `/auth`

| Metodo | Endpoint publico | Endpoint interno | Descricao |
| --- | --- | --- | --- |
| `POST` | `/auth/login` | `/auth/login` | Login e emissao de token |
| `GET` | `/auth/validate` | `/auth/validate` | Validacao de token usada pelo Traefik |
| `GET` | `/auth/health` | `/health` | Health check do auth |

Payload de login:

```json
{
  "email": "user@example.com",
  "password": "secret"
}
```

## Users Service

Prefixo publico: `/users`

O Traefik remove `/users` antes de encaminhar para o servico. Exemplo: `/users/admins` chega no app como `/admins`.

### Admins

| Metodo | Endpoint publico | Endpoint interno | Descricao |
| --- | --- | --- | --- |
| `POST` | `/users/admins/` | `/admins/` | Cria admin |
| `GET` | `/users/admins/` | `/admins/` | Lista admins |
| `GET` | `/users/admins/{user_id}` | `/admins/{user_id}` | Detalha admin |
| `PUT` | `/users/admins/{user_id}` | `/admins/{user_id}` | Atualiza admin |
| `DELETE` | `/users/admins/{user_id}` | `/admins/{user_id}` | Remove admin |

### Atendents

| Metodo | Endpoint publico | Endpoint interno | Descricao |
| --- | --- | --- | --- |
| `POST` | `/users/atendents/` | `/atendents/` | Cria atendente |
| `GET` | `/users/atendents/` | `/atendents/` | Lista atendentes |
| `GET` | `/users/atendents/{user_id}` | `/atendents/{user_id}` | Detalha atendente |
| `PUT` | `/users/atendents/{user_id}` | `/atendents/{user_id}` | Atualiza atendente |
| `DELETE` | `/users/atendents/{user_id}` | `/atendents/{user_id}` | Remove atendente |

### Medics

| Metodo | Endpoint publico | Endpoint interno | Descricao |
| --- | --- | --- | --- |
| `POST` | `/users/medics/` | `/medics/` | Cria medico |
| `GET` | `/users/medics/` | `/medics/` | Lista medicos |
| `GET` | `/users/medics/{user_id}` | `/medics/{user_id}` | Detalha medico |
| `PUT` | `/users/medics/{user_id}` | `/medics/{user_id}` | Atualiza medico |
| `DELETE` | `/users/medics/{user_id}` | `/medics/{user_id}` | Remove medico |

### Pacients

| Metodo | Endpoint publico | Endpoint interno | Descricao |
| --- | --- | --- | --- |
| `POST` | `/users/pacients/` | `/pacients/` | Cria paciente |
| `GET` | `/users/pacients/` | `/pacients/` | Lista pacientes |
| `GET` | `/users/pacients/{user_id}` | `/pacients/{user_id}` | Detalha paciente |
| `PUT` | `/users/pacients/{user_id}` | `/pacients/{user_id}` | Atualiza paciente |
| `DELETE` | `/users/pacients/{user_id}` | `/pacients/{user_id}` | Remove paciente |

### Health

| Metodo | Endpoint publico | Endpoint interno | Descricao |
| --- | --- | --- | --- |
| `GET` | `/users/health` | `/health` | Health check do users service |

Payload de criacao de usuario:

```json
{
  "userName": "dr.house",
  "email": "house@example.com",
  "name": "Gregory House",
  "password": "password123"
}
```

Payload de atualizacao de usuario:

```json
{
  "userName": "dr.house",
  "email": "house@example.com",
  "name": "Gregory House",
  "password": "password123"
}
```

Todos os campos de atualizacao sao opcionais.

## Agenda Service

Prefixo publico e interno: `/agenda`

### Appointments

| Metodo | Endpoint publico | Descricao |
| --- | --- | --- |
| `POST` | `/agenda/appointments/` | Cria appointment |
| `GET` | `/agenda/appointments/` | Lista appointments. Query: `limit`, `offset` |
| `GET` | `/agenda/appointments/{appointment_id}` | Detalha appointment |
| `PUT` | `/agenda/appointments/{appointment_id}` | Atualiza appointment |
| `DELETE` | `/agenda/appointments/{appointment_id}` | Remove appointment |

Payload de criacao:

```json
{
  "scheduler_id": "scheduler-1",
  "date": "2026-06-02",
  "weekday": "tuesday",
  "doctor": "doctor-1",
  "patient": "patient-1",
  "time": "09:00",
  "type": "consultation",
  "room": "room-1"
}
```

### Calendars

| Metodo | Endpoint publico | Descricao |
| --- | --- | --- |
| `POST` | `/agenda/calendars/` | Cria calendario mensal |
| `GET` | `/agenda/calendars/days` | Lista dias. Query: `year`, `month`, `limit`, `offset` |
| `GET` | `/agenda/calendars/days/{day_id}` | Detalha dia |
| `PATCH` | `/agenda/calendars/days/{day_id}` | Atualiza dados do dia |
| `DELETE` | `/agenda/calendars/{ano}` | Remove calendario por ano |

Payload de criacao:

```json
{
  "mes": 6,
  "ano": 2026
}
```

Payload de atualizacao de dia:

```json
{
  "id": "day-1",
  "data": {}
}
```

### Clinics

| Metodo | Endpoint publico | Descricao |
| --- | --- | --- |
| `POST` | `/agenda/clinics/` | Cria clinica |
| `GET` | `/agenda/clinics/` | Lista clinicas. Query: `limit`, `offset` |
| `GET` | `/agenda/clinics/{clinic_id}` | Detalha clinica |
| `PUT` | `/agenda/clinics/{clinic_id}` | Atualiza clinica |
| `DELETE` | `/agenda/clinics/{clinic_id}` | Remove clinica |

Payload:

```json
{
  "name": "Clinica Central",
  "rules": []
}
```

### Doctors

| Metodo | Endpoint publico | Descricao |
| --- | --- | --- |
| `POST` | `/agenda/doctors/` | Cria medico |
| `GET` | `/agenda/doctors/` | Lista medicos. Query: `limit`, `offset` |
| `GET` | `/agenda/doctors/{doctor_id}` | Detalha medico |
| `PUT` | `/agenda/doctors/{doctor_id}` | Atualiza medico |
| `DELETE` | `/agenda/doctors/{doctor_id}` | Remove medico |

Payload de criacao:

```json
{
  "id_extern": "303",
  "name": "Dr Delete"
}
```

Payload de atualizacao:

```json
{
  "id": "303",
  "name": "Dr Delete",
  "availability": true,
  "rules": []
}
```

### Patients

| Metodo | Endpoint publico | Descricao |
| --- | --- | --- |
| `POST` | `/agenda/patients/` | Cria paciente |
| `GET` | `/agenda/patients/` | Lista pacientes. Query: `limit`, `offset` |
| `GET` | `/agenda/patients/{patient_id}` | Detalha paciente |
| `PUT` | `/agenda/patients/{patient_id}` | Atualiza paciente |
| `DELETE` | `/agenda/patients/{patient_id}` | Remove paciente |

Payload de criacao:

```json
{
  "id": "404",
  "name": "Patient Delete"
}
```

### Rooms

| Metodo | Endpoint publico | Descricao |
| --- | --- | --- |
| `POST` | `/agenda/rooms/` | Cria sala |
| `GET` | `/agenda/rooms/` | Lista salas. Query: `limit`, `offset` |
| `GET` | `/agenda/rooms/{room_id}` | Detalha sala |
| `PUT` | `/agenda/rooms/{room_id}` | Atualiza sala |
| `DELETE` | `/agenda/rooms/{room_id}` | Remove sala |

Payload de criacao:

```json
{
  "name": "Sala 1"
}
```

### Rules

| Metodo | Endpoint publico | Descricao |
| --- | --- | --- |
| `GET` | `/agenda/rules/` | Lista regras. Query: `limit`, `offset` |
| `GET` | `/agenda/rules/{rule_id}` | Detalha regra |
| `POST` | `/agenda/rules/block` | Cria regra de bloqueio |
| `POST` | `/agenda/rules/generic` | Cria regra generica |
| `POST` | `/agenda/rules/specific` | Cria regra especifica |
| `POST` | `/agenda/rules/specific-day` | Cria regra especifica de dia |
| `POST` | `/agenda/rules/week` | Cria regra semanal |
| `DELETE` | `/agenda/rules/{rule_id}` | Remove regra |

### Infra

| Metodo | Endpoint publico | Descricao |
| --- | --- | --- |
| `GET` | `/agenda/infra/health` | Health/config do modulo de infra |
| `POST` | `/agenda/infra/events/users/doctor-created` | Handler manual para evento de criacao de medico vindo do user service |
| `POST` | `/agenda/infra/events/users/patient-created` | Handler manual para evento de criacao de paciente vindo do user service |
| `POST` | `/agenda/infra/events/users/doctor-deleted` | Handler manual para evento de delete de medico vindo do user service |
| `POST` | `/agenda/infra/events/users/patient-deleted` | Handler manual para evento de delete de paciente vindo do user service |

### Websocket

| Protocolo | Endpoint publico | Descricao |
| --- | --- | --- |
| `WS` | `/agenda/ws` | Canal websocket do agenda service |

## Notification Service

Prefixo publico: `/notification`

O Traefik remove `/notification` antes de encaminhar para o servico.

### Email

| Metodo | Endpoint publico | Endpoint interno | Descricao |
| --- | --- | --- | --- |
| `POST` | `/notification/email/send` | `/email/send` | Envia email |
| `GET` | `/notification/email/sent` | `/email/sent` | Lista emails enviados |

Payload de envio:

```json
{
  "to": "patient@example.com",
  "subject": "Consulta confirmada",
  "body": "Sua consulta foi confirmada.",
  "metadata": {}
}
```

### User Notifications

| Metodo | Endpoint publico | Endpoint interno | Descricao |
| --- | --- | --- | --- |
| `POST` | `/notification/notifications/` | `/notifications/` | Cria notificacao |
| `GET` | `/notification/notifications/users/{user_id}` | `/notifications/users/{user_id}` | Lista notificacoes do usuario |
| `GET` | `/notification/notifications/users/{user_id}/unread-count` | `/notifications/users/{user_id}/unread-count` | Conta nao lidas |
| `PATCH` | `/notification/notifications/{notification_id}/read` | `/notifications/{notification_id}/read` | Marca notificacao como lida |
| `PATCH` | `/notification/notifications/users/{user_id}/read-all` | `/notifications/users/{user_id}/read-all` | Marca todas como lidas |
| `GET` | `/notification/health` | `/health` | Health check do notification service |

Payload de notificacao:

```json
{
  "user_id": "404",
  "title": "Consulta",
  "message": "Sua consulta foi criada.",
  "link": "/agenda/appointments/123",
  "metadata": {}
}
```

## Analytics Service

Prefixo publico e interno: `/analytics`

| Metodo | Endpoint publico | Descricao |
| --- | --- | --- |
| `GET` | `/analytics/doctors/{doctor_id}/dashboard` | Dashboard do medico |
| `GET` | `/analytics/operations/business/dashboard` | Dashboard operacional de negocio |
| `GET` | `/analytics/operations/platform/dashboard` | Dashboard operacional de plataforma |
| `GET` | `/analytics/health` | Health check do analytics service |
| `GET` | `/analytics/metrics` | Metricas Prometheus do analytics service |

## Observabilidade e Infraestrutura

Esses servicos continuam publicados por porta direta no `docker-compose.yml`:

| Servico | URL local | Observacao |
| --- | --- | --- |
| Traefik dashboard | `http://localhost:8080` | Dashboard administrativo do Traefik |
| RabbitMQ management | `http://localhost:15672` | UI de gerenciamento do RabbitMQ |
| OpenFGA API | `http://localhost:8090` | API HTTP do OpenFGA |
| OpenFGA Playground | `http://localhost:3000` | Playground do OpenFGA |
| Grafana | `http://localhost:3001` | Disponivel com profile `observability` |
| Prometheus | `http://localhost:9090` | Disponivel com profile `observability` |
