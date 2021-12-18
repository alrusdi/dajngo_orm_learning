from django.db.models import Q
from texttable import Texttable

from shooting1.models import Result


def show_results():
    results = get_results3()

    table = Texttable()
    table.add_row(["Место", "Город", "Стрелок", "Результат"])
    for idx, res in enumerate(results):
        table.add_row([idx+1, res.shooter.city.name, res.shooter.name, res.result])
    print(table.draw())


# Таблица результатов с сыном мера
def get_results1():
    results = Result.objects.order_by("-result")
    results = results.exclude(Q(shooter__city__name="Москва", result__lte=380) & ~Q(shooter__name="Собянин Виктор"))
    return results


# Таблица результатов со стрелками Марк и Кирилл
def get_results2():
    results = Result.objects.order_by("-result")
    results = results.filter(Q(shooter__name__endswith="Марк") | Q(shooter__name__endswith="Кирилл"))
    return results


# Таблица результатов со именами стрелков из переданного списка
def get_results3(names=["Максим", "Марк", "Али"]):
    results = Result.objects.order_by("-result")
    filter_by_names = Q()
    for name in names:
        filter_by_names |= Q(shooter__name__endswith=name)
    results = results.filter(filter_by_names)
    return results


# Выделение фильтров в отдельную функцию
def get_filtered_results(city_names=None, search_by_player_name=None, minimal_result=380):
    results = Result.objects.order_by("-result")

    filter_query = filter_results_queryset(city_names, search_by_player_name, minimal_result)

    results.filter(**filter_query)

    # А версию с рефакториного мприменим так:
    # filter_query_set = filter_results_queryset_refactored(city_names, search_by_player_name, minimal_result)
    # results.filter(filter_query_set)

    return results


# Фильтрующая часть большого запроса для отчета
def filter_results_queryset(city_names=None, search_by_player_name=None, minimal_result=380):
    query = {}

    if city_names:
        query["shooter__city__name__in"] = city_names

    if search_by_player_name:
        query["shooter__name__ilike"] = search_by_player_name

    if minimal_result:
        query["resuts__gte"] = minimal_result

    return query


# Фильтрующая часть большого запроса для отчета с помощью объекта Q
def filter_results_queryset_refactored(city_names=None, search_by_player_name=None, minimal_result=380):
    query_set = Q()

    if city_names:
        query_set &= Q(shooter__city__name__in=city_names)

    if search_by_player_name:
        query_set &= Q(shooter__name__ilike=city_names)

    if minimal_result:
        query_set &= Q(reqult__gte=minimal_result)

    # Посмотреть какой получился запрос на данный момент можно так:
    print(query_set.query)

    return query_set
