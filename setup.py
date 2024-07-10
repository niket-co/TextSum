import setuptools
with open("README.md", "r", encoding="utf-8") as f:
              long_description = f.read()  ##Appears if published as a pypi package


__version__ = "0.0.0"

REPO_NAME = "TextSum"
AUTHOR_USER_NAME = "niket-co"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "niket620535@gmail.com"

setuptools.setup(
        name=SRC_REPO,
        version=__version__,
        author=AUTHOR_USER_NAME,
        author_email= AUTHOR_EMAIL,
        description="A small python package for NLP app",
        long_description=long_description,
        long_description_content="text/markdown",
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        project_urls={
                "Bug_Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        },
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src")
)