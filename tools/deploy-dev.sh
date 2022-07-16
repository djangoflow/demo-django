#!/bin/sh
export KUBECONFIG=~/.kube/demo-dev_kubeconfig.yaml \
	&& sh tools/cloudbuild.sh src \
	&& kubectl delete po -n demo-dev -l app.kubernetes.io/name=django