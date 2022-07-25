#!/bin/sh
export KUBECONFIG=~/.kube/demo-django_kubeconfig.yaml \
	&& sh tools/cloudbuild.sh src \
	&& kubectl delete po -n demo -l app.kubernetes.io/name=django
