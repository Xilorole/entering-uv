# https://github.com/cli/cli/issues/6096
if [[ $(command -v gh) ]]; then
    # The workaround needs user scope and at least for corporate accounts, that isn't the default
    gh auth refresh -h github.com -s user

    user=$(gh api -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" /user | jq -r .login)
    email=$(gh api -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" /user/emails | jq -r ".[0].email")
    echo "Setting $user <$email> as the default Git user..."
    git config user.name "$user"
    git config user.email "$email"
fi
