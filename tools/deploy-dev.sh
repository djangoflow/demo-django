#!/bin/sh
export KUBECONFIG=~/.kube/dfc_kubeconfig.yaml \
	&& sh tools/cloudbuild.sh src \
	&& kubectl delete po -n ae -l app.kubernetes.io/part-of=django
