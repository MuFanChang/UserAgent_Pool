from setuptools import setup, find_packages

setup(
    name = 'UserAgentPool',
    version = '1.0.3',
    description = 'Use for randomly get header',
    author = 'Steven Chang',
    author_email = 's8110282004@gmail.com',
    url = 'https://github.com/MuFanChang/UserAgentPool',
    download_url = 'https://github.com/MuFanChang/UserAgentPool/releases/tag/v1.0.2',
    scripts = 'UserAgent.py',
    packages = find_packages(),
    keywords = ['UserAgent','header'],
    classifiers = []
)