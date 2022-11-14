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

testing with flake8 by

- install flake8
  ```
  pip install flake8
  ```
- running flake8
  ```
  flake8 .
  ```

> are flake8 configuration cannot be changed 


### ⚠️NOTE⚠️
if you encountered an issue when running pip, try running pip with higher privilege using sudo

## contribution guideline
* any changes that you made need to output such that
* use `snake_case` when naming a file

## Pull Request
to avoid conflict with other pull request, use [*issue*](https://github.com/slowy07/luna/issues) when adding or modifying a file

* explain to us in the [*issue*](https://github.com/slowy07/luna/issues) what you want to change or add in detail
* after you explain to us what changes you want to make in the [*issue*](https://github.com/slowy07/luna/issues), then you can create your own fork of our repository
* after creating your own fork of the repo, feel free to add or change    you are free to add and modify the proposed changes in the fork
* after you are finish, make sure to create a new local branch, and then commit the changes like so: 
``` 
git checkout -b <branch_name>
git add . 
git commit -m "feat: adding new feature on luna which can ..."
```
* push the changes you made to the new branch, then open a pull request to our repo

### commit message

and make sure to add these prefixes on your commit message
* `feat:` when you add a new algorithm;
* `fix:` when you changed or fixed an already existing algorithm;
* `docs:` when you change or create a documentation;
* `add:` when you add an algorithm or other stuff;

note: make sure the message included in the commit message is summarized, like so

- ❌ feat: test_x.py
- ✅ feat: adding changes for ``file.py`` and create some change on ...

#### breaking changes!
if you made a breaking changes, make sure to add `BREAKING CHANGE:` in the footer,\
or append ! (exclamation mark) infront of prefix like so `!feat: new encoding`

click [here](https://www.conventionalcommits.org/en/v1.0.0/) for more information regarding commit


pull request will only be merge IF:
- it follows the `CONTRIBUTING.md` guidelines
- it passed the test that we have provided

additional:
- if you encountered an issue on a pull request, you can report it via [*issue*](https://github.com/slowy07/luna/issues)
- and if you failed our test, we will re-evaluate your changes
- for pull request it is advisable to be polite and nice to other, because that's how programmer should behafe from one to another
