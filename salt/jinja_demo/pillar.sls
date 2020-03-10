
{%- set mysecret = pillar.get('mysecret', 'somedefault') %}

set_mysecret:
  file.managed:
    - name: /demo/secret.txt
    - contents: "{{ mysecret }}"
