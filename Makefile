# self-documentation magic: http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help: ## Display the list of available targets
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: clean
clean:
	rm -rf .cache .coverage dist build

.PHONY: downloads
downloads:
	curl -L https://pypi.org/pypi/lektor-ng/json > support/tests/data/pypi.json
#	gh api repos/cav71/lektor-ng/actions/runs/31253031694/logs > z.zip
#	gh run list -R cav71/lektor-ng --limit 1 --json databaseId --jq '.[0].databaseId' > z.id && \
#    gh api repos/cav71/lektor-ng/actions/runs/$(shell cat z.id)/logs > z.zip

.PHONY: tests
tests: export PYTHONPATH=$(PWD)/src
tests:  ## run the support tests
	uv run pytest -vvs tests

.PHONY: release
release:  ## test release builder
	python support/builder.py $@ \
      --pypidata support/tests/data/pypi.json \
      --gitdump support/tests/data/$@.gitdump.json --dump

post:  ## test release builder
	python support/builder.py $@ --post-if-released \
      --pypidata support/tests/data/pypi.json \
      --gitdump support/tests/data/release.gitdump.json --dump
