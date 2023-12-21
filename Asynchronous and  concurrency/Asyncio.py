import asyncio

# Fonction qui sera appelée lorsqu'un événement se produit


async def handle_event(event):
    print(f"Événement reçu : {event}")
    # Effectuer des actions en fonction de l'événement

# Simuler la génération d'événements


async def generate_events():
    for i in range(1, 6):
        await asyncio.sleep(1)  # Attendre 1 seconde
        event = f"Événement {i}"
        # Appeler la fonction de traitement de l'événement
        await handle_event(event)

# Lancer la boucle principale asyncio


async def main():
    await generate_events()

# Lancer l'application event-driven
asyncio.run(main())
