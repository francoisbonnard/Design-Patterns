Voici une liste de 30 concepts courants en conception de systèmes (system design) avec, pour chacun, une définition en français et un exemple concret pour mieux les illustrer.

---

## 1. Client-Server Architecture
**Définition :**  
Une architecture client-serveur sépare les rôles entre des clients (qui envoient des requêtes) et des serveurs (qui fournissent des réponses ou des services). Le client exécute généralement l’interface utilisateur et dépend du serveur pour des données ou des fonctionnalités.

**Exemple :**  
- Lorsque vous utilisez un navigateur web (client) pour accéder à un site web (serveur), vous envoyez une requête HTTP au serveur. Celui-ci renvoie alors la page web à votre navigateur pour affichage.

---

## 2. IP Address
**Définition :**  
Une adresse IP (Internet Protocol) est une suite de nombres permettant d’identifier de manière unique un appareil sur un réseau (Internet ou réseau local). Elle peut être au format IPv4 (ex: 192.168.0.1) ou IPv6 (ex: 2001:0db8:85a3::8a2e:0370:7334).

**Exemple :**  
- Votre ordinateur, lorsque connecté à votre box Internet, se voit attribuer une adresse IP locale (par exemple 192.168.1.10). Les serveurs publics (comme un serveur web) ont une adresse IP publique (par exemple 93.184.216.34).

---

## 3. DNS (Domain Name System)
**Définition :**  
Le DNS est le « répertoire téléphonique » d’Internet. Il convertit des noms de domaine lisibles (ex: google.com) en adresses IP (ex: 142.250.185.14) que les machines utilisent pour se connecter entre elles.

**Exemple :**  
- Quand vous tapez `www.example.com` dans votre navigateur, le DNS va trouver l’adresse IP associée (par exemple 93.184.216.34) et diriger votre requête vers le serveur correspondant.

---

## 4. Proxy / Reverse Proxy
**Définition :**  
- **Proxy (direct) :** un serveur intermédiaire qui relaie les requêtes des clients vers un serveur en leur nom. Il peut être utilisé pour la mise en cache, l’anonymisation ou le filtrage.
- **Reverse Proxy :** un serveur intermédiaire qui se place devant un ou plusieurs serveurs internes. Il reçoit les requêtes externes et les distribue aux serveurs en arrière-plan. Il sert à équilibrer la charge, sécuriser l’accès ou mettre en cache les contenus.

**Exemple :**  
- **Proxy (direct) :** dans une entreprise, tout le trafic web des employés peut passer par un proxy qui bloque certains sites ou met en cache les pages fréquemment visitées.  
- **Reverse Proxy :** Nginx peut être configuré comme reverse proxy devant plusieurs serveurs d’applications, gérant la répartition de la charge et la sécurité.

---

## 5. Latency
**Définition :**  
La latence est le temps de transit ou de réponse entre l’envoi d’une requête et la réception de la première réponse. En d’autres termes, c’est le délai ressenti par l’utilisateur lorsqu’il interagit avec un système.

**Exemple :**  
- Quand vous cliquez sur un lien dans votre navigateur, si le serveur est géographiquement éloigné ou très chargé, vous pouvez ressentir une latence plus élevée (temps plus long avant que la page ne commence à se charger).

---

## 6. HTTP/HTTPS
**Définition :**  
- **HTTP (HyperText Transfer Protocol) :** protocole de communication pour le transfert de données (pages web, ressources, etc.) sur Internet.  
- **HTTPS (HTTP Secure) :** variante sécurisée de HTTP qui chiffre les données échangées entre le client et le serveur (via TLS/SSL), garantissant la confidentialité et l’intégrité.

**Exemple :**  
- Les sites comme `http://example.com` utilisent HTTP simple, alors que `https://example.com` chiffrera la communication pour protéger les données de l’utilisateur (ex: mots de passe, informations bancaires).

---

## 7. APIs (Application Programming Interfaces)
**Définition :**  
Une API est un ensemble de définitions et de protocoles qui permet à des applications ou des services de communiquer entre eux. Elle décrit comment les fonctionnalités d’un logiciel peuvent être utilisées par d’autres programmes.

**Exemple :**  
- L’API de Google Maps permet à des développeurs tiers d’intégrer des cartes ou des fonctionnalités de localisation dans leurs propres applications (sites de réservation de voyages, applications mobiles, etc.).

---

## 8. REST API
**Définition :**  
Une API REST (Representational State Transfer) suit un style d’architecture où l’on utilise principalement les verbes HTTP (GET, POST, PUT, DELETE, etc.) pour manipuler des ressources identifiées par des URI. Les réponses sont souvent au format JSON ou XML.

**Exemple :**  
- Une API REST de gestion de produits e-commerce avec des endpoints comme :  
  - `GET /products` (récupère la liste des produits)  
  - `POST /products` (ajoute un nouveau produit)  
  - `GET /products/{id}` (récupère un produit spécifique)

---

## 9. GraphQL
**Définition :**  
GraphQL est un langage de requête et un runtime côté serveur qui permet aux clients de spécifier précisément les données dont ils ont besoin. Cela évite de surcharger le client avec des données non nécessaires et de multiplier les requêtes.

**Exemple :**  
- Une requête GraphQL pour récupérer un utilisateur et sa liste de publications pourrait ressembler à :  
  ```graphql
  {
    user(id: "123") {
      name
      posts {
        title
        content
      }
    }
  }
  ```
  Le serveur renvoie uniquement les champs demandés (name, title, content).

---

## 10. Databases
**Définition :**  
Une base de données est un système de stockage et d’organisation de données, permettant d’effectuer des opérations de lecture, d’écriture et de mise à jour. On distingue principalement les bases de données relationnelles (SQL) et non relationnelles (NoSQL).

**Exemple :**  
- MySQL, PostgreSQL (bases relationnelles)  
- MongoDB, Cassandra (bases NoSQL)

---

## 11. SQL vs NoSQL
**Définition :**  
- **SQL (Structured Query Language) :** bases de données relationnelles organisées en tables avec des relations entre elles. Les données respectent un schéma fixe.  
- **NoSQL :** bases de données non relationnelles (clé-valeur, documents, colonnes larges, graphes). Elles offrent plus de flexibilité de schéma et sont souvent plus faciles à scaler horizontalement.

**Exemple :**  
- **SQL :** MySQL, PostgreSQL (utilise des tables, colonnes, lignes).  
- **NoSQL :** MongoDB (stocke des documents JSON), Redis (stockage clé-valeur en mémoire).

---

## 12. Vertical Scaling
**Définition :**  
Le scaling vertical (mise à l’échelle verticale) consiste à augmenter la capacité d’un serveur unique en lui ajoutant plus de ressources (CPU, RAM, stockage). Cela revient à « faire grossir » la machine.

**Exemple :**  
- Passer d’un serveur 2 cœurs/4 Go de RAM à un serveur 8 cœurs/16 Go de RAM pour supporter plus de charges.

---

## 13. Horizontal Scaling
**Définition :**  
Le scaling horizontal (mise à l’échelle horizontale) consiste à ajouter plus de serveurs ou de nœuds pour répartir la charge. On multiplie le nombre de machines plutôt que d’augmenter la puissance d’une seule.

**Exemple :**  
- Au lieu d’avoir un seul gros serveur, on utilise un cluster de plusieurs serveurs plus petits. Par exemple, ajouter 10 serveurs à 2 cœurs/4 Go de RAM chacun, et répartir le trafic.

---

## 14. Load Balancers
**Définition :**  
Un équilibreur de charge (load balancer) est un composant réseau qui distribue le trafic entrant sur plusieurs serveurs, afin d’optimiser l’utilisation des ressources, la disponibilité et les performances.

**Exemple :**  
- Nginx ou HAProxy peuvent être configurés pour diriger intelligemment le trafic HTTP vers différents serveurs web en fonction de leur disponibilité ou de leur charge.

---

## 15. Database Indexing
**Définition :**  
L’indexation en base de données consiste à créer des structures de données (index) pour accélérer les recherches et les opérations de tri sur des colonnes spécifiques. Les index permettent de retrouver plus rapidement les lignes correspondantes à un critère.

**Exemple :**  
- Sur une table `users` avec une colonne `email`, la création d’un index sur `email` permettra d’accélérer les requêtes du type `SELECT * FROM users WHERE email = 'exemple@domaine.com'`.

---

## 16. Replication
**Définition :**  
La réplication consiste à dupliquer les données d’une base (ou d’un système) sur plusieurs serveurs afin d’augmenter la tolérance aux pannes et/ou d’améliorer les performances (lecture depuis plusieurs réplicas).

**Exemple :**  
- Un cluster MySQL peut avoir un serveur principal (master) qui gère les écritures, et plusieurs réplicas (slaves) qui reçoivent une copie des données pour gérer les lectures.

---

## 17. Sharding
**Définition :**  
Le sharding (ou partitionnement horizontal) consiste à diviser une base de données volumineuse en plusieurs morceaux (shards) distribués sur différents serveurs. Chaque shard contient un sous-ensemble des données, souvent déterminé par une clé de partition (ex: ID utilisateur).

**Exemple :**  
- Dans une application avec des millions d’utilisateurs, on peut répartir les utilisateurs en fonction de leur ID. Les utilisateurs ayant un ID de 1 à 1 million sont stockés sur le shard A, ceux de 1 million à 2 millions sur le shard B, etc.

---

## 18. Vertical Partitioning
**Définition :**  
Le partitionnement vertical sépare les colonnes d’une table en différentes bases ou différentes tables, souvent pour isoler des champs peu utilisés ou plus volumineux. Cela peut améliorer les performances en lecture/écriture sur les champs principaux.

**Exemple :**  
- Dans une table `users` contenant de nombreuses colonnes (profil, historique, préférences, etc.), on peut déplacer les colonnes d’historique volumineuses dans une table ou base séparée pour réduire la taille de la table principale.

---

## 19. Caching
**Définition :**  
Le caching (mise en cache) consiste à stocker temporairement des données fréquemment demandées dans une mémoire plus rapide (RAM, CDN, etc.) pour réduire les temps d’accès et la charge sur les ressources plus lentes (base de données, disque dur).

**Exemple :**  
- Utiliser Redis ou Memcached pour stocker les résultats de requêtes complexes. Ainsi, si la même requête arrive peu de temps après, on renvoie la réponse depuis le cache au lieu de recalculer la requête en base.

---

## 20. Denormalization
**Définition :**  
La dénormalisation consiste à dupliquer des données dans une base (souvent relationnelle) afin de réduire le nombre de jointures et d’améliorer les performances de lecture. Cela va à l’encontre de la normalisation stricte, mais peut être utile à grande échelle.

**Exemple :**  
- Au lieu d’avoir une table `orders` et une table `customers` séparées, on peut stocker directement le nom du client dans la table `orders` (au lieu de faire une jointure) pour accélérer les requêtes de lecture sur les commandes.

---

## 21. CAP Theorem
**Définition :**  
Le théorème CAP (Consistency, Availability, Partition tolerance) indique qu’un système distribué ne peut pas fournir simultanément ces trois garanties à 100 % : cohérence (Consistency), disponibilité (Availability) et tolérance aux partitions (Partition Tolerance). Il faut choisir deux de ces propriétés, au détriment de la troisième.

**Exemple :**  
- Un système de base de données qui privilégie la cohérence et la tolérance aux partitions (CP) peut sacrifier la disponibilité en cas de réseau partitionné. Par exemple, certains modes de Cassandra ou de MongoDB peuvent être configurés en CP.

---

## 22. Blob Storage
**Définition :**  
Le stockage de type BLOB (Binary Large OBject) est un service de stockage d’objets volumineux (images, vidéos, fichiers) dans des conteneurs ou buckets. Il permet de gérer de grands volumes de données non structurées.

**Exemple :**  
- Amazon S3, Google Cloud Storage ou Azure Blob Storage sont des solutions de stockage d’objets où l’on peut uploader des images, des documents ou des backups de bases de données.

---

## 23. CDN (Content Delivery Network)
**Définition :**  
Un CDN est un réseau de serveurs géographiquement distribués qui stockent en cache (ou répliquent) des contenus statiques (images, fichiers CSS/JS, vidéos). L’objectif est de rapprocher physiquement le contenu des utilisateurs pour réduire la latence et accélérer le chargement.

**Exemple :**  
- Cloudflare ou Akamai peuvent servir les images d’un site web à partir d’un serveur proche de l’utilisateur, plutôt que de toujours solliciter le serveur d’origine situé dans un autre pays.

---

## 24. WebSockets
**Définition :**  
WebSocket est un protocole de communication bidirectionnelle et en temps réel entre le client et le serveur. Contrairement à HTTP, la connexion reste ouverte, permettant au serveur d’envoyer des données au client sans que celui-ci ne doive faire une nouvelle requête.

**Exemple :**  
- Les applications de chat en temps réel (ex: Slack, Discord) ou les tableaux de bord boursiers utilisent des WebSockets pour mettre à jour instantanément les messages ou les données de cours.

---

## 25. Webhooks
**Définition :**  
Un webhook est un mécanisme permettant à une application d’envoyer une requête HTTP à une autre application dès qu’un événement spécifique se produit. C’est un moyen de notification push.

**Exemple :**  
- Lorsqu’un utilisateur fait un paiement sur PayPal, PayPal peut envoyer un webhook à votre serveur pour vous informer du paiement. Votre application peut alors mettre à jour automatiquement le statut de la commande.

---

## 26. Microservices
**Définition :**  
Les microservices sont une approche de développement où l’application est divisée en petits services indépendants, chacun gérant une fonctionnalité métier précise, et communiquant souvent via des APIs légères. Cela facilite la scalabilité, la flexibilité et la maintenance.

**Exemple :**  
- Un site e-commerce peut avoir un microservice « catalogue de produits », un microservice « commandes », un microservice « paiements » et un microservice « notifications », tous développés et déployés séparément.

---

## 27. Message Queues
**Définition :**  
Les files de messages (Message Queues) permettent à différentes parties d’un système de communiquer de manière asynchrone en s’envoyant des messages. L’émetteur place un message dans la file, et le récepteur le traite plus tard, ce qui découple fortement les services.

**Exemple :**  
- RabbitMQ, Apache Kafka ou AWS SQS : on peut envoyer un message « nouvelle commande » dans une file. Un service de facturation consomme ce message pour créer la facture, tandis qu’un autre service de notification envoie un email, etc.

---

## 28. Rate Limiting
**Définition :**  
Le rate limiting (limitation de débit) est une technique pour restreindre le nombre de requêtes qu’un client peut effectuer sur une période donnée, afin d’éviter les abus ou les surcharges (DDos, brute force, etc.).

**Exemple :**  
- Une API publique peut autoriser seulement 100 requêtes par minute et par adresse IP. Si un client dépasse ce seuil, il reçoit une réponse d’erreur (HTTP 429 « Too Many Requests »).

---

## 29. API Gateways
**Définition :**  
Un API Gateway est un point d’entrée unique pour toutes les requêtes vers les microservices ou les APIs d’un système. Il peut gérer l’authentification, le routage, la transformation des requêtes/réponses, le rate limiting, etc.

**Exemple :**  
- AWS API Gateway ou Kong peuvent servir de façade unique pour un ensemble de microservices. Les clients ne communiquent qu’avec l’API Gateway, qui se charge de rediriger la requête vers le bon service.

---

## 30. Idempotency
**Définition :**  
Une opération est idempotente si son exécution plusieurs fois produit le même résultat que son exécution une seule fois. En d’autres termes, répéter l’opération n’a pas d’effets supplémentaires ou néfastes.

**Exemple :**  
- Dans un système de paiement, une requête pour « annuler une transaction » doit être idempotente : si vous appelez deux fois l’endpoint « annuler », le résultat doit rester le même (la transaction est annulée, et il ne se passe rien de plus si on réessaie).

---

**En résumé**, ces concepts forment la base de la conception de systèmes distribués et d’applications web/mobiles à grande échelle. Chacun répond à des problématiques spécifiques (scalabilité, fiabilité, performance, etc.) et ils sont souvent combinés pour créer des architectures robustes et évolutives.