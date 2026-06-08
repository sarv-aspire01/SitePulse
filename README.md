# SitePulse

SitePulse is a lightweight website monitoring system designed to continuously (at a regular interval) track websites, news portals, recruitment portals, government notification pages, university notice boards, and other frequently updated websites.

The project is built around a simple goal: automatically detect meaningful updates on websites without maintaining a dedicated VPS or cloud server. Instead of relying on external monitoring services, SitePulse uses GitHub Actions as its execution environment, Telegram as its notification channel, and repository persistence to maintain monitoring state between runs.

## workflow
Targets → Fetch → Extract → Compare → Notify → Save State

Targets are defined in YAML configuration files and executed through a GitHub Actions workflow. Each run fetches the configured pages, extracts relevant content, compares it with previously stored snapshots, and generates alerts when changes are detected.

To avoid external infrastructure, monitoring state and snapshots are stored in the repository under data/ and automatically updated after each run. GitHub Secrets are used to securely manage Telegram bot credentials and other sensitive configuration.

### CI/CD Pipeline

GitHub Actions automates the monitoring workflow by:

* Loading targets from `config/`.
* Securely accessing bot credentials via GitHub Secrets.
* Running the monitoring pipeline via modules in `src/`.
* Comparing extracted content against snapshots stored in `data/snapshots/`.
* Sending change, failure, and health notifications via Telegram.
* Saving updated snapshots and suppression state under `data/`.
* Persisting monitoring state by automatically committing and pushing repository updates.



# How To Use

Although the public project is intended for collaboration and development, My recommendation is to **fork this repository and make your fork private before configuring any real targets or github secrets**.

#### Configure Targets

Targets are stored in YAML configuration files inside:

```text
config/
```

Example:

```yaml
- name: Example site
  category: company
  url: https://www.example.com
  selector: body
```

### Configure Telegram Notification

Create a Telegram bot using:
@BotFather, 
Copy the generated bot token, 
Send a message to the bot and obtain your chat ID.
now open your private repository and add the following GitHub Secrets:

```text
Settings
 └── Secrets and Variables
     └── Actions
```

Required secrets:
```text
TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID
```

### GitHub Actions

> **Note:** Automated scheduling is currently disabled. Uncomment the all codes inside `sitepulse.yml` to enable periodic monitoring.

Monitoring is done via:

```text
.github/workflows/sitepulse.yml
```
#### Scheduling

Cron-based execution like:

```yaml
# Every 6 hours
0 */6 * * *

# Daily
0 0 * * *
```

#### Manual Execution

```text
Actions → SItePulse Monitoring System → Run Workflow
```

# Building Further & Contributing

The project currently includes following modules in `src/`. Each module focuses on a single responsibility, making it easier to replace or extend functionality without affecting the entire pipeline.

```text
fetcher.py
extractor.py
detector.py
storage.py
notifier.py
main.py
```

## Local Development

Clone and run in VS Code:

```bash
git clone https://github.com/sarv-aspire01/SitePulse
cd SitePulse
code .
```

Install dependencies (in venv):

```bash
pip install -r requirements.txt
```
- Configure `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` in `.env`.

Run locally:

```bash
python3 src/main.py
```

## Testing

The `tests/` directory contains unit tests used during development to validate individual modules.

Run all tests:

```bash
pytest tests/
```

Changes to any existing/new components must be accompanied by updated or additional tests.

## Contributing

If you would like to improve the project:

1. Fork the repository.
2. Create a feature branch.
3. Implement and test changes.
4. Open a Pull Request.

areas for future work:

* Better SSL handling
* Retry and backoff strategies
* Parallel fetching
* Advanced diff visualization
* Additional notification providers (like email)
* Dashboard and reporting features

Contributions, bug reports, feature ideas, and discussions are always welcome.
