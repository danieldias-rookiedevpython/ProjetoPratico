from fastapi import APIRouter, Depends, status

from src.api.provider import (
    get_create_block_rule_use_case,
    get_create_generic_rule_use_case,
    get_create_specific_day_rule_use_case,
    get_create_specific_rule_use_case,
    get_create_week_rule_use_case,
    get_delete_rule_use_case,
    get_list_rules_query_use_case,
    get_rule_by_id_query_use_case,
)
from src.modules.agenda.aplication.dtos.useCase.command.RulesUseCasesDTO import (
    CreateBlockRuleCommand,
    CreateGenericRuleCommand,
    CreateSpecificDayRuleCommand,
    CreateSpecificRuleCommand,
    CreateWeekRuleCommand,
)
from src.modules.agenda.aplication.dtos.useCase.query import GetByIdQuery, ListQuery


routerRule = APIRouter(prefix="/rules", tags=["Rules"])


@routerRule.get("/")
async def list_rules(
    limit: int | None = None,
    offset: int = 0,
    use_case=Depends(get_list_rules_query_use_case),
):
    return await use_case.execute(ListQuery(limit=limit, offset=offset))


@routerRule.get("/{rule_id}")
async def get_rule(rule_id: str, use_case=Depends(get_rule_by_id_query_use_case)):
    return await use_case.execute(GetByIdQuery(id=rule_id))


@routerRule.post("/block", status_code=status.HTTP_201_CREATED)
async def create_block_rule(command: CreateBlockRuleCommand, use_case=Depends(get_create_block_rule_use_case)):
    return {"created": await use_case.execute(command)}


@routerRule.post("/generic", status_code=status.HTTP_201_CREATED)
async def create_generic_rule(command: CreateGenericRuleCommand, use_case=Depends(get_create_generic_rule_use_case)):
    return {"created": await use_case.execute(command)}


@routerRule.post("/specific", status_code=status.HTTP_201_CREATED)
async def create_specific_rule(command: CreateSpecificRuleCommand, use_case=Depends(get_create_specific_rule_use_case)):
    return {"created": await use_case.execute(command)}


@routerRule.post("/specific-day", status_code=status.HTTP_201_CREATED)
async def create_specific_day_rule(
    command: CreateSpecificDayRuleCommand,
    use_case=Depends(get_create_specific_day_rule_use_case),
):
    return {"created": await use_case.execute(command)}


@routerRule.post("/week", status_code=status.HTTP_201_CREATED)
async def create_week_rule(command: CreateWeekRuleCommand, use_case=Depends(get_create_week_rule_use_case)):
    return {"created": await use_case.execute(command)}


@routerRule.delete("/{rule_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_rule(rule_id: str, use_case=Depends(get_delete_rule_use_case)):
    await use_case.execute(rule_id)
