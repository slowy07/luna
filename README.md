# luna
text to image generation with stable diffusion

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

![astronut_horse](.github/result_output/astronaut_horse.png)

###  other output

> God wearing mask

![god_wearing_mask](.github/result_output/god_wearing_mask.png)

> Harry potter random

![harry_potter_random](.github/result_output/harry_potter_random.png)

> Marilyn monroe with random  art style

![marilyn_monroe_with_random_art_style](.github/result_output/marilyn_monroe_with_random_art_style.png)

