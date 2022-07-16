#!/bin/sh
TARGET=${1:-.}
BRANCH_NAME="${CI_COMMIT_REF_NAME:-latest}"
[ "${CI_COMMIT_REF_NAME}" == "main" ] && BRANCH_NAME='latest'
echo "Building ${TARGET} ${BRANCH_NAME}"
gcloud builds submit --project=demo "${TARGET}" --config="${TARGET}"/cloudbuild.yaml --substitutions=BRANCH_NAME=${BRANCH_NAME}