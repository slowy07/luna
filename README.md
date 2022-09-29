# luna
![code_quality_checking](https://img.shields.io/github/workflow/status/slowy07/luna/CodeQL?label=Code%20quality%20check&style=flat-square)
![python_post_processing](https://img.shields.io/github/workflow/status/slowy07/luna/PythonPostPorcessing?label=Python%20Post%20Processing&style=flat-square)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=flat-square&logo=TensorFlow&logoColor=white)


Stable diffusion is a deep learning, text-to-image model and used to generate detailted images
conditioned on text description, thout it can also be applied to other task such as inpainting or outpainting and 
generate image to image translate guide by text prompt.

**try online on google colab**: 

luna can running on online colab notebook you can check here:

- [luna](https://colab.research.google.com/drive/1IyHaYLCPLRurVs-tJJRLbCcO4kr1xlOi?usp=sharing)
- [luna with gpu and mixed precision](https://colab.research.google.com/drive/1ydFWPt6BgPT7i4VmZcs8ttGaFu7dw-cV?usp=sharing) 
  - 15 seconds generation time per image (512 x 512) on default colab GPU without drop the quality


**usage for online colab**:

- click the connect
  ![connect](./github/connect.png)
- open on ``runtime`` and click run all ( ``ctrl+f9`` if using shortcut )
  ![running](./github/running.png)
- online collab running luna



# usage
### use venv
```
//create venv
python3 -m venv venv

//activate venv
source venv/bin/activate
```

### clone repo
clone on https :
```
git clone https://github.com/slowy07/luna
cd luna
pip install -r requirements.txt
```

clone on ssh :
```
git clone git@github.com:slowy07/luna.git
cd luna
pip install -r requirements.txt
```

**note** : if using mac m1 you can try installing the ``requirements_m1.txt``

### run script
```
python text2image.py --prompt="example text"
```
to change the output file name run using the `--output` flag
```
python text2image.py --prompt="cool picture" --output="cool_pic.png"
```


###  install as python package
```
pip install git+https://github.com/slowy07/luna
```
and run the package using
```python
from stable_diffusion_tensorflow.stable_diffusion import Text2Image

generator = Text2Image(img_height=512, img_width=512, jit_compose=False)
img = generator.generate(
  "DSLR photograph of an astronut ridinga horse",
  num_steps = 50,
  unconditional_guidance_scale = 75,
  temperature = 1,
  batch_size = 1,
)
```

you can change dimension of image by change the ``img_height`` and ``img_width``

```python
generator = Text2Image(
  img_height = 1020 # or change 1080
  img_height = 1080 # or change 800
)
```

### ⚠️ NOTE ⚠️
if pip encountered an issue, try running pip with higher privilege using `sudo`

# output

```python
img = generator.generate(
  "DSLR photograph of an astronut ridinga horse",
  num_steps = 50,
  unconditional_guidance_scale = 75,
  temperature = 1,
  batch_size = 1,
)
```
output:

| description | image |
| ------ | ----- |
| prompt: DSLR photograph of an astronut ridinga horse | ![astronut_horse](.github/result_output/astronaut_horse.png) |
| prompt: DSLR photograph of an astronut ridinga horse with unconditional_guidance_scale 7.5 | ![astronaut_horse2](.github/result_output/astronaut_horse2.png) |
| prompt: DSLR photograph of an astronut ridinga horse with unconditional_guidance_scale 7.5 | ![astronaut_horse3](.github/result_output/astronaut_horse3.png) |
| prompt: DSLR photograph of an astronut ridinga horse with unconditional_guidance_scale 7.5 | ![astronaut_horse4](.github/result_output/astronaut_horse4.png) |

###  other output

```python
image_prompt: str = "Harry potter playing basketball"
img = generator.generate(
  image_prompt,
  num_steps = 50,
  unconditional_guidance_scale = 5.6,
  temperature = 1,
  batch_size = 1,
)
```

| description | image |
| ------ | ----- |
| prompt: indonesia country with cyberpunk style | ![indonesia_country_with_cyberpunk_style](.github/result_output/indonesia_country_with_cyberpunk_style.png) |
| prompt: medival castle realistic and detailed oil painting | ![medival_castle_realistic_and_detailed_oil_painting](.github/result_output/medival_castle_realistic_and_detailed_oil_painting.png) |
| prompt: harry potter playing basketball | ![harry_potter_playing_basketball](.github/result_output/harry_potter_playing_basket.png) |
| prompt: harry potter playing guitar     | ![harry_potter_playing_guitar](.github/result_output/harry_potter_playing_guitar.png)     |
| prompt: person hacking with computer    | ![person_hacking_with_computer](.github/result_output/person_hacking_with_computer.png) |
| prompt: God wearing mask | ![god_wearing_mask](.github/result_output/god_wearing_mask.png) |
| prompt: Harry potter random | ![harry_potter_random](.github/result_output/harry_potter_random.png) |
| prompt: Marilyn monroe with random  art style | ![marilyn_monroe_with_random_art_style](.github/result_output/marilyn_monroe_with_random_art_style.png) |

---

### donate

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/arfyslowy)

