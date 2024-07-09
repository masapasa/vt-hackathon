import json
from iiif_prezi3 import Manifest, config
import requests

# Set up the manifest
config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

manifest = Manifest(id="https://iiif.archive.org/iiif/3/sim_manifesto_1878-05_8_5/manifest.json",
                    label={"en": ["The Manifesto 1871-1899, May 1878"]},
                    behavior=["paged"])

# Create canvas
canvas = manifest.make_canvas_from_iiif(
    url="https://iiif.archive.org/iiif/sim_manifesto_1878-05_8_5$13/full/full/0/default.jpg",
    id="https://iiif.archive.org/iiif/3/sim_manifesto_1878-05_8_5/canvas/p13",
    label="Page 13",
    anno_id="https://iiif.archive.org/iiif/3/sim_manifesto_1878-05_8_5/annotation/p13-image",
    anno_page_id="https://iiif.archive.org/iiif/3/sim_manifesto_1878-05_8_5/page/p13/1"
)

# Create annotation
annotation = canvas.make_annotation(
    id="https://iiif.archive.org/iiif/3/sim_manifesto_1878-05_8_5/annotation/p13-text",
    motivation="commenting",
    body={
        "type": "TextualBody",
        "language": "en",
        "format": "text/plain",
        "value": "owrs, temptation"
    },
    target=f"{canvas.id}#xywh=349,640,799,1211",
    anno_page_id="https://iiif.archive.org/iiif/3/sim_manifesto_1878-05_8_5/page/p13/1"
)

# Print the manifest JSON
print(manifest.json(indent=2))