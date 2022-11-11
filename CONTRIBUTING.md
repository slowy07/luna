# *Contributing*

***Contributor***

Lets contribute !!!

but before you start contributing here are some rules and guide you need to follow
* we only accept original code that you made, any code that has a simularity to any online sources won't be merge !
* your work will be licensed as [MIT](LICENSE) after merge
* follow style and code conventions that we have provided in the guideline
<!-- * we only accept file with `*.py` extension -->

## installation

### use venv (optional)
create and activate new virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### clone repo

clone with https or ssh
```bash
git clone https://github.com/slowy07/luna
```
or
```bash
 git clone git@github.com:slowy07/luna.git
```
then open the folder and install all the dependencies
```bash
cd luna
pip install -r requirements.txt
```
**note** : if your are using mac m1 and encounter an error, try using the `requirements_m1.txt` instead

and run the script
```bash
python text2image.py --prompt="example text"
# if you want to change the output file you can use the `--output` flag, and add the new filename like so
python text2image.py --prompt="cool picture" --output="cool_pic.png"
```

### install as python package
or install it as python package
```bash
pip install git+https://github.com/slowy07/luna
```
then create a script like so
```py
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
you can also change the dimension of the generated image like so
```py
generator = Text2Image(
  img_height = 1020 # or change 1080
  img_height = 1080 # or change 800
)
```
### ⚠️NOTE⚠️
if you encountered an issue when running pip, try running pip with higher privilege using sudo

## contribution guideline
* any changes that you made need to output such that
* use `snake_case` when naming a file
* every tutorial or implementation need to be in the same folder, like so:

```
count_variable
├── README.md (description)
├── countvariable.py
```

## Pull Request
to avoid conflict with other pull request, use [*issue*](https://github.com/slowy07/luna/issues) when adding or modifying a file

* explain to us in the [*issue*](https://github.com/slowy07/luna/issues) what you want to change or add in detail
* after you explain to us what changes you want to make in the [*issue*](https://github.com/slowy07/luna/issues), then you can create your own fork of our repository
* after creating your own fork of the repo, feel free to add or change    you are free to add and modify the proposed changes in the fork
* after you are finish, make sure to create a new local branch, and then commit the changes like so: 
``` 
git checkout -b <branch_name>
git add . # atau git add nama_perubahan_kamu.py
git commit -m "feat: menambahkan tutorial terbaru"
```
* push the changes you made to the new branch, then open a pull request to our repo

### commit message
and make sure to add these prefixes on your commit message
* `feat:` when you add a new algorithm
* `fix:` when you changed or fixed an already existing algorithm;
* `docs:` when you change or create a documentation;
* `add:` when you add an algorithm or other stuff;

note: make sure the message included in the commit message is summarized, like so

- ❌ feat: test_x.py
- ✅ feat: added a unittest for algorithm x

click here for more information regarding this
- [EN](https://www.conventionalcommits.org/en/v1.0.0/)
- [ID](https://www.conventionalcommits.org/id/v1.0.0/)

pull request will be merge IF!:
- it follows the `CONTRIBUTING.md` guidelines
- it passed the test that we have provided

additional:
- if you encountered an issue on a pull request, you can report it via [*issue*](https://github.com/slowy07/luna/issues)
- and if you failed our test, we will re-evaluate your changes
- for pull request it is advisable to be polite and nice to other, because that's how programmer should behafe from one to another
