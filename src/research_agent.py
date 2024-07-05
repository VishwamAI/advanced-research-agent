import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import time
import gym
from stable_baselines3 import PPO

class ResearchAgentEnv(gym.Env):
    def __init__(self):
        super(ResearchAgentEnv, self).__init__()
        self.action_space = gym.spaces.Discrete(2)  # Example: 2 actions (e.g., parse paragraphs, parse headers)
        self.observation_space = gym.spaces.Discrete(2)  # Example: 2 states (e.g., page with paragraphs, page with headers)
        self.state = 0
        self.data = []

    def reset(self):
        self.state = 0
        self.data = []
        return self.state

    def step(self, action):
        reward = 0
        done = False
        if action == 0:
            # Example: Parse paragraphs
            reward = 1  # Example reward
        elif action == 1:
            # Example: Parse headers
            reward = 1  # Example reward
        self.state = (self.state + 1) % 2
        return self.state, reward, done, {}

    def render(self, mode='human'):
        pass

class ResearchAgent:
    def __init__(self):
        self.data = []
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.env = ResearchAgentEnv()
        self.model = PPO('MlpPolicy', self.env, verbose=1)
        self.model.learn(total_timesteps=1000)

    def fetch_page(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching {url}: {e}")
            return None

    def parse_page(self, html_content, action):
        soup = BeautifulSoup(html_content, 'html.parser')
        if action == 0:
            # Example: Extracting all paragraph texts
            paragraphs = soup.find_all('p')
            for p in paragraphs:
                self.data.append(p.get_text())
        elif action == 1:
            # Example: Extracting all header texts
            headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            for header in headers:
                self.data.append(header.get_text())

    def save_data(self, filename):
        df = pd.DataFrame(self.data, columns=['Content'])
        df.to_csv(filename, index=False)

    def run(self, url, output_file):
        html_content = self.fetch_page(url)
        if html_content:
            action = self.model.predict(self.env.state)[0]
            self.parse_page(html_content, action)
            self.save_data(output_file)
        else:
            logging.error("Failed to retrieve the page.")

    def run_with_rate_limiting(self, urls, output_file, delay=1):
        for url in urls:
            self.run(url, output_file)
            time.sleep(delay)

if __name__ == "__main__":
    agent = ResearchAgent()
    test_urls = ["https://example.com", "https://example.org"]
    output_file = "output.csv"
    agent.run_with_rate_limiting(test_urls, output_file, delay=2)
