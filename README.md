# Djangoflow demo Django project.

Full-stack cross-platform applications in weeks, not months. (And prototypes in days, not weeks).

## Summary

DjangoFlow (DF) is an opinionated backend-as-a-service platform for creating, developing, deploying
and managing Django[tm] projects that comes with batteries included. And that means a set of matching
client-side modules for Flutter[tm] that seamlessly integrate with DF.

The mission of DF is to automate repetitive tasks that are common to many Django projects,
allowing developers to focus / spend their time on project specifics instead.

DF project structure is uniform and opinionated in order to allow external management by DF.
Outside these restrictions DF projects can vary from dynamic e-commerce sites to headless
rest/graphql application backends.

A typical usage of DF would be:

- create a new Django project with a single form
- add required plugins, such as authentication, notifications etc
- setup integrations by following integration wizards (e.g. Firebase, Facebook, Apple Signin, Stripe, Twilio)
- create a local development environment and develop custom modules
- create a staging environment and deploy with a single click

DF combines and integrates a number of proven technologies and open source frameworks such as:

- Git - GitHub/GitLab
- CSP - Cloud Service Provider - GCP, AWS, Azure
- Kubernetes
- Terraform
- Templating - copier

## Components

- DF core (wip) - a web-app to manage DF projects
- DF Django project template - a copier template to bootstrap a project
- DF Flutter app template - a template to bootstrap a flutter project
- DF Django modules - plugins for additional functionality
- DF Flutter packages - matching flutter packages to work with DJ Django modules
- DF Terraform - terraform template and modules to deploy a DF project to cloud

## DF Django Project Structure

A DF project is structured in a predefined way to allow easy tooling, CI and deployment.

A DF project is built as two separate Docker images, a base image containing all the requirements and scripts (which
are not changed often); and actual project image, that is based on the above, and adds the project source code (which
are changed more often, so we avoid full image rebuild this way).

The above is reflected in the project structure:
```
/
├── .idea               - pre-generated IntelliJ IDEA config
├── README.md           - project wide README
├── base                - base image, requirements.txt, Dockerfile, scripts, etc
├── docs                - documentation
├── src                 - main sources
└── tools               - project wide tools / scripts
```

The `src` is the Django top level folder containing the `manage.py` script and further organised as:

```
src/
├── apps/               - project specific applications
├── config/             - project settings, url and certain common files 
├── locale/             - translations and localisation
├── static/             - project wide static files, such as assets, css and js
├── templates/          - project specific templates (base, pages, emails, pdf etc)
├── Dockerfile          - main sources Dockerfile
├── manage.py
├── pytest.ini          - test & pre-commit
└── setup.cfg           - test & pre-commit
```

The  `config` contains standard django project files as urls, storages, settings etc.

Settings and urls are further organised into `deployments` (for a lack of better term k8s terminology), i.e.:

```
config/
├── sections/           - common sections to be included
├── local/              - local configuration for development 
├── web/                - configuration for serving web
├── admin/              - configuration for serving admin site
├── api/                - configuration for serving api
└── wsgi.py             - wsgi application
```


Template TODO:

[ ] Create reasonable defaults for IDEA
[ ] Pre-commit hooks
[ ] Github CI


## Entities

- Project - a single django project managed by DF
- Stack - a terraform stack (deployment)
- Environment - a (cloud) environment a project can be deployed to managed with terraform
- Platform - a platform for deployment either local (e.g. docker) or cloud e.g. GCP)
- VCS - a version control system for a project
- Integration - a managed integration with an external service like FCM or Stripe
- Plugin - a python module with DF metadata managed by DF, a plugin can provide own Integration or operate with an existing one
- Setting - an individual setting for a Project, Integration or Plugin that can be either in-code, environment or secret
