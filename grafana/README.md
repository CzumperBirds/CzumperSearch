# Grafana - local development (localhost)


## Set up

1. You need to create your own github access token in your github account in order to connect dashboard to **grafana-github-datasource**
- Login to your GitHub account.
- Navigate to Personal access tokens and click Generate new token.
- Select the personal access token (classic).
- Define the permissions which you want to allow.
- Click Generate Token.
- **COPY YOUR TOKEN to clickboard !!!**

Official documentation guide:
    
>https://grafana.com/docs/plugins/grafana-github-datasource/latest/setup/token/

2. Then you need to update **.env** file in the grafana directory ''**/grafana/.env**'':

Paste here your password and copied github-token created in previous step
```shell
# .env
GF_SECURITY_ADMIN_PASSWORD=<password_for_admin_grafana> # <--
GF_INSTALL_PLUGINS=grafana-github-datasource
GF_GITHUB_TOKEN=<your_token_from_step_1> # <--
GF_GITHUB_OWNER=CzumperBirds
GF_GITHUB_REPO=CzumperSearch
```
Login and password to grafana(default): admin


## Usage - (Start Up)
To start grafana simply run :

```shell
make prod-up
```

or with verbose (not detached mode)
```shell
make prod-upv
```

- to deep clear grafana run:
```shell
make prod-delete
```

## Add dashboards
1. When you modify existing dashboard you can save its JSON locally (on host machine)
and paste it in **/grafana/provisioning/dashboards** directory. 
It will automatically import it after restart.