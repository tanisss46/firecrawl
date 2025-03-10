# Enable autocompletion for the Stripe CLI

## Enable autocompletion so that the Stripe CLI automatically completes your commands.

Use the `stripe completion` command to enable autocompletion so that the Stripe
CLI automatically completes your commands. After you enable autocomplete, you
can type a command and press the tab key on your keyboard to view available
commands and flags.

## Setup with ZSH on macOS and Linux

Open a new ZSH shell and run the following commands:

```
stripe completion
mkdir -p ~/.stripe
mv stripe-completion.zsh ~/.stripe
```

Add the following lines to your `.zshrc` file:

```
# The next lines enables shell command completion for Stripe
fpath=(~/.stripe $fpath)
autoload -Uz compinit && compinit -i
```

## Setup with Bash on macOS and Linux

Follow the instructions in
[bash-completion](https://formulae.brew.sh/formula/bash-completion/) to set up
bash completions.

Open a new Bash shell and run the following commands:

```
stripe completion
mkdir -p ~/.stripe
mv stripe-completion.bash ~/.stripe
```

Add the following lines to your `.bashrc` file:

```
# The next line enables shell command completion for Stripe
source ~/.stripe/stripe-completion.bash
```

## Windows

Windows autocompletion is currently not supported.

## Links

- [bash-completion](https://formulae.brew.sh/formula/bash-completion/)