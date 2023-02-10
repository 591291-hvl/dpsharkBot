import os
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

import random

os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

os.environ[
    'STABILITY_KEY'] = 'sk-imGfcKIU41LLDMxtcxbY3HgINeIWjAd6opgECrz5996HmG4Q'

stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'],  # API Key reference.
    verbose=True,  # Print debug messages.
    engine="stable-diffusion-v1-5",  # Set the engine to use for generation.
)


def send_promt(ask_promt):
    answers = stability_api.generate(prompt=ask_promt,
                                     steps=30,
                                     cfg_scale=8.0,
                                     width=512,
                                     height=512,
                                     samples=1,
                                     sampler=generation.SAMPLER_K_DPMPP_2M)

    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.save('other/newImage.png')


keyWords = [
    [
        "Ocean",
        "The vast ocean stretched out endlessly, its depths hiding unknown mysteries.",
        "The dynamic waves of the ocean crashed against the shore, shaping the land.",
        "The oceanscape was adorned with a brilliant array of marine life and coral reefs.",
        "The pristine waters of the ocean shimmered in the sunlight, inviting for a swim.",
        "The unpredictable ocean currents and storms made it a powerful and formidable force."
    ],
    [
        "Mountain",
        "The towering peak, shrouded in mist, loomed above the valley below.",
        "The jagged ridges of the mountain range stretched out as far as the eye could see.",
        "The snow-covered summit glistened in the sunlight, beckoning adventurers to conquer its heights.",
        "The rocky outcroppings of the mountain provided a natural fortress, defying the elements for centuries."
    ],
    [
        "Forest",
        "The dense canopy of the forest blocked out the sun, creating a mysterious and enchanting atmosphere.",
        "The towering trees of the forest reached up to the sky, providing a home for diverse wildlife.",
        "The lush undergrowth of the forest was a riot of color and life, teeming with plants and animals.",
        "The serene stillness of the forest was only occasionally broken by the call of birds and the rustling of leaves.",
        "The ancient trees of the forest stood sentinel, their roots deep in the earth, their branches brushing the sky."
    ],
    [
        "River",
        "The sparkling water of the river flowed gracefully, carving its way through the landscape.",
        "The tranquil surface of the river was ruffled by the gentle breeze and the occasional fish jumping.",
        "The winding path of the river was surrounded by lush greenery and diverse wildlife.",
        "The soothing sound of the river's flow provided a backdrop for the peaceful countryside.",
        "The life-giving water of the river sustained the plants, animals and the community living along its banks."
    ],
    [
        "Fjord",
        "The steep cliffs of the fjord rose dramatically from the cold, dark waters.",
        "The winding inlet of the fjord was surrounded by snow-capped peaks and glaciers.",
        "The tranquil surface of the fjord was dotted with small islands and surrounded by dense forests.",
        "The fjord's dark, mysterious waters were home to a variety of marine life and hidden caves.",
        "The natural beauty of the fjord created a breathtaking landscape that was both awe-inspiring and humbling."
    ],
    [
        "Desert",
        "The vast expanse of the desert stretched out endlessly, its sands rippling in the relentless sun.",
        "The barren landscape of the desert was punctuated by towering dunes and rocky outcroppings.",
        "The scorching heat of the desert made it a harsh and unforgiving environment for those who dared to venture there.",
        "The silence of the desert was only broken by the howling winds and the occasional cry of a desert animal.",
        "The stark beauty of the desert was both mesmerizing and intimidating, with its endless horizon and endless sand."
    ],
    [
        "Volcano",
        "The towering volcano loomed over the landscape, its smoldering crater a constant reminder of its power.",
        "The fiery lava flowed down the volcano's slopes, carving a path of destruction in its wake.",
        "The ash and smoke from the volcano filled the air, creating a dark and ominous atmosphere.",
        "The explosive eruptions of the volcano sent rocks and debris flying, making it a dangerous and unpredictable force.",
        "The primal energy of the volcano, both destructive and creation, was a reminder of the raw power of nature."
    ],
    [
        "Lake",
        "The serene waters of the lake reflected the surrounding landscape, creating a mirror-like surface.",
        "The tranquil atmosphere of the lake was a haven for those seeking peace and solitude.",
        "The crystal clear water of the lake was teeming with fish and aquatic life.",
        "The beauty of the lake was enhanced by the gentle swaying of the reeds and the colorful flowers on its shore.",
        "The calmness of the lake was only broken by the occasional splash of a jumping fish or the gentle lapping of the waves."
    ],
    [
        "Waterfall",
        "The powerful rush of water cascaded down the cliffs, creating a mesmerizing curtain of mist.",
        "The thundering roar of the waterfall echoed through the surrounding wilderness.",
        "The sparkling water of the waterfall glistened in the sunlight, creating a rainbow of colors.",
        "The mist and spray of the waterfall created a cool and refreshing oasis in the heat of the day.",
        "The raw energy and power of the waterfall was both awe-inspiring and humbling."
    ],
    [
        "Valley",
        "The picturesque valley was nestled between rolling hills and majestic mountains.",
        "The lush greenery of the valley was dotted with colorful wildflowers and verdant fields.",
        "The peaceful tranquility of the valley was only broken by the gentle sound of a flowing stream.",
        "The secluded valley provided a sanctuary for an array of wildlife and birds.",
        "The natural beauty of the valley was a breathtaking sight, with its panoramic views and its serenity."
    ]
]


def findKeyword(sentence):
    words = sentence.split()  #Og noe her med split
    for i in range(len(keyWords)):
        for j in range(len(words)):
            if keyWords[i][0].lower() == words[j].lower():
                words[j] = keyWords[i][random.randint(1, len(keyWords[i])-1)]
    print(words)
    return ' '.join(words)


def wrapper(input):
    send_promt(findKeyword(input))
