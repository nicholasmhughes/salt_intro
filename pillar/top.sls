
base:
  '*':
    - all
  'os_family:RedHat':
    - match: grain
    - rhel_secrets
