import re
from iiif_prezi3 import Manifest

def extract_xywh(page_image_url):
    match = re.search(r'pct:(\d+\.\d+),(\d+\.\d+),(\d+\.\d+),(\d+\.\d+)', page_image_url)
    if match:
        x, y, w, h = map(float, match.groups())
        return f"#xywh={x:.0f},{y:.0f},{w:.0f},{h:.0f}"
    return None

def create_canvas_and_annotation(manifest, image_url, canvas_id, label, anno_id, anno_page_id, page_image_url=None):
    canvas = manifest.make_canvas_from_iiif(
        url=image_url,
        id=canvas_id,
        label=label,
        anno_id=anno_id,
        anno_page_id=anno_page_id
    )

    xywh = "#xywh=265,661,1260,1239"  # Default value
    if page_image_url:
        extracted_xywh = extract_xywh(page_image_url)
        if extracted_xywh:
            xywh = extracted_xywh

    anno = canvas.make_annotation(
        id=f"{canvas_id}/annotation",
        motivation="tagging",
        body={
            "type": "TextualBody",
            "language": "en",
            "format": "text/plain",
            "value": "Here is another annotation"
        },
        target=f"{canvas.id}{xywh}",
        anno_page_id=anno_page_id
    )

    return canvas, anno

# Example usage
manifest = Manifest(id="https://example.com/manifest.json", label={"en": ["Example Manifest"]})

image_url = "https://tile.loc.gov/image-services/iiif/service:ndnp:oru:batch_oru_hufnagel_ver02:data:sn96061150:00200298111:1889102001:0369"
canvas_id = "https://iiif.io/api/cookbook/recipe/0009-book-1/canvas/p2"
label = "The daily morning Astorian. [volume], October 20, 1889"
anno_id = "https://iiif.io/api/cookbook/recipe/0009-book-1/annotation/p0002-image"
anno_page_id = "https://www.loc.gov/resource/sn96061150/1889-10-20/ed-1/seq-2/"

# Example with page_image_url
page_image_url = "https://chroniclingamerica.loc.gov/iiif/2/service%2Fndnp%2Fme%2Fbatch_me_camden_ver01%2Fdata%2Fsn78000873%2F00279524688%2F1878110701%2F0198.jp2/pct:4.509507,83.684080,11.277974,1.872369/full/0/default.jpg"

canvas, anno = create_canvas_and_annotation(manifest, image_url, canvas_id, label, anno_id, anno_page_id, page_image_url)

print(f"Canvas ID: {canvas.id}")
print(f"Annotation target: {anno.target}")