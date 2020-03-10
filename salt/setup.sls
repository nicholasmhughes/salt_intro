
remove_files:
  file.absent:
    - names:
      - /var/cache/salt/minion/extmods/modules/weather.py
      - /var/cache/salt/minion/extmods/modules/weather.pyc
      - /var/cache/salt/master/roots/hash/base/_modules/weather.py.hash.sha256

/demo:
  file.directory:
    - mode: '0755'

/demo/permissions.txt:
  file.managed:
    - user: root
    - group: root

/demo/append.txt:
  file.managed:
    - contents: |
        This is the first line
