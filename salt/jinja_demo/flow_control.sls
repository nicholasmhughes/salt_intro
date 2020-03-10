
{%- set myconfigs = pillar.get('myconfigs', {}) %}

{%- for key, value in myconfigs | dictsort %}
{%-   if key != "dog_night" %}
echo_{{key}}config_for_no_reason:
  cmd.run:
    - name: echo "{{ key }} is set to {{ value }}"

{%    endif -%}
{%- endfor %}
