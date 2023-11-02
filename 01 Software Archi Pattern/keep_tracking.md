## Source

https://www.infoq.com/
https://dzone.com/refcardz
    

## technology radar

https://www.thoughtworks.com/radar
![Alt text](image.png)


## Design System
https://www.thoughtworks.com/radar/techniques/design-system-decision-records

##  Design System Decisions

Architecture Description Records (ADRs) 
[capturing Design System decisions](https://zeroheight.com/blog/capturing-your-design-system-decisions/)

## gitflow vs trunk-based
https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development

## YAGNI : You ain't gonna need it

Don't overengineer

## scaling

### vertical or horizontal

### State or Stateless 

### Cap theorem

for DB

Which consistency Level ?
- Strict consistency : any write immediately available for all users
- eventual consistency : delay between the write and availability

Le théorème CAP (Consistency, Availability, Partition tolerance) est un concept clé en informatique distribuée qui met en avant les limitations des systèmes distribués. Selon ce théorème, un système distribué ne peut garantir simultanément les trois propriétés suivantes :

1. **Consistency (Consistance)** : Toutes les parties du système voient les mêmes données au même moment. En d'autres termes, chaque lecture sur le système renverra le même résultat, indépendamment de l'endroit où cette lecture est effectuée.

2. **Availability (Disponibilité)** : Chaque requête (lecture ou écriture) reçoit une réponse, sans garantie que celle-ci contient les données les plus récentes ou les plus cohérentes. En d'autres termes, le système répond même si certaines parties de celui-ci sont en panne.

3. **Partition tolerance (Tolérance aux partitions)** : Le système continue de fonctionner même si des messages sont perdus ou si les nœuds du système sont séparés en plusieurs groupes incapables de communiquer les uns avec les autres (c'est-à-dire en cas de panne réseau).

Lorsque l'on parle d'**"eventual consistency" (consistance éventuelle)**, on se réfère à la capacité d'un système distribué à garantir la cohérence des données à long terme, même s'il peut y avoir des retards temporaires dans la propagation des mises à jour à travers le système. En d'autres termes, le système peut subir des incohérences temporaires, mais finira par atteindre un état cohérent à mesure que les mises à jour se propagent à travers le système.

Ce modèle de consistance est souvent utilisé dans les systèmes distribués où la disponibilité et la tolérance aux partitions sont des priorités, comme les systèmes de bases de données NoSQL. Ces systèmes préfèrent offrir une disponibilité continue même en cas de perte de cohérence momentanée entre les nœuds, et la cohérence des données est garantie à long terme à mesure que le système se rétablit après une partition réseau ou une panne.



Reads vs Writes

Next / https://www.youtube.com/watch?v=gxfERVP18-g&list=PL4JxLacgYgqTgS8qQPC17fM-NWMTr5GW6&index=2


### horizontal scaling

Sharing or replication

Data sharding (split data between country)

Sharding by hash (for user id)


## Event Sourcing

CQRS / split read & write