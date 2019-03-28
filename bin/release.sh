#!/bin/bash
current_branch=$(git rev-parse --abbrev-ref HEAD)
git checkout master
git push origin master --tags
git checkout stable
git merge master
git push origin stable
git checkout $current_branch
