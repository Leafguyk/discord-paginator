from setuptools import setup, find_packages
 
setup(
    # ������ ��Ű���� �̸��� �����ݴϴ�. setup.py������ ������ ���� �̸��� �����ϰ� �մϴ�.
    name                = 'discord_paginator',
    # ������ ��Ű���� ������ �����ݴϴ�. ù ����̹Ƿ� 0.1 �Ǵ� 0.0.1�� ����մϴ�.
    version             = '0.1',
    # ������ ��Ű���� ���� ������ �ۼ��մϴ�.
    description         = 'discord paginator developed by Leafguyk',
    # �����ϴ� ����� �̸��� �ۼ��մϴ�.
    author              = 'Leafguyk',
    # �����ϴ� ����� �����ּҸ� �ۼ��մϴ�.
    author_email        = 'leafguykk@gmail.com',
    # �����ϴ� ��Ű���� url�� �����ݴϴ�. ���� github ��ũ�� �����ϴ�.
    url                 = 'https://github.com/Leafguyk/discord_paginator',
    # �����ϴ� ��Ű���� �ٿ�ε� url�� �����ݴϴ�.
    download_url        = 'https://github.com/Leafguyk/discord_paginator/archive/refs/heads/main.zip',
    # �ش� ��Ű���� ����ϱ� ���� �ʿ��� ��Ű���� �����ݴϴ�. ex. install_requires= ['numpy', 'django']
    # ���⿡ ������ ��Ű���� ���� ��Ű���� install�Ҷ� �Բ� install�˴ϴ�.
    install_requires    =  ['discord.py','discord-py-interactions','discord-py-slash-command'],
    # ����ϰ��� �ϴ� ��Ű���� ���� ���Դϴ�.
    # �츮�� find_packages ���̺귯���� �̿��ϱ� ������ �Ʒ��� ���� �����ݴϴ�.
    # ���� �����ϰ��� �ϴ� ������ �ִٸ� exclude�� �����ݴϴ�.
    packages            = find_packages(exclude = []),
    # ��Ű���� Ű���带 �����ϴ�.
    keywords            = ['discord'],
    # �ش� ��Ű���� ����ϱ� ���� �ʿ��� ���̽� ������ �����ϴ�.
    python_requires     = '>=3',
    # ���̽� ������ �ƴ� �ٸ� ������ ���Խ�Ű�� �ʹٸ� package_data�� ���Խ��Ѿ� �մϴ�.
    package_data        = {},
    # ���� package_data�� ���� ������ �Ͽ��ٸ� zip_safe������ ���־�� �մϴ�.
    zip_safe            = False,
    # PyPI�� ��ϵ� ��Ÿ �����͸� �����մϴ�.
    # �̴� �ܼ��� PyPI�� ��ϵǴ� ��Ÿ �������� ���̰�, ���� ���忡�� ������ ���� �ʽ��ϴ�.
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

