from execute_util import link, image, text
from arxiv_util import arxiv_reference
from lecture_util import article_link, x_link, youtube_link
from reference import join
from references import previous_share_on_rl, agentic_rl_landscape, qwen_tool_call, rstar_agent


def main():
    welcome()
    what_is_this_program()
    # The Landscape of Agentic Reinforcement Learning for LLMs: A Survey
    difference_between_llm_rl_and_agentic_rl()
    capability_perspective()
    vertical_domains()
    # A tool call example based on Qwen
    link(title="A Tool Demo Based on Qwen3", url="https://donpromax.github.io/trace-viewer/?trace=var%2Ftraces%2Ftool_call_example.json")
    
    rstar2_agent()
    # rStar2-Agent demo
    link(title="rStar2 Agent Demo", url="https://donpromax.github.io/trace-viewer/?trace=var%2Ftraces%2Frstar_agent.json")


def welcome():
    text("## Sharing Insights on Training and Inference in Agentic Reinforcement Learning")
    text("- Previous Sharing on Reinforcement Learning"), link(previous_share_on_rl)
    image("images/agentic/rl.png", width=600)
    text("### Overview of today's topic")
    text("- The Landscape of Agentic Reinforcement Learning for LLMs: A Survey"), link(agentic_rl_landscape)
    text("- A tool call example based on Qwen&nbsp;"), link(qwen_tool_call)
    text("- rStar2-Agent: Agentic Reasoning Technical Report"), link(rstar_agent)


def what_is_this_program():
    text("This is an *executable lecture*, a program whose execution delivers the content of a lecture.")
    text("Executable lectures make it possible to:")
    text("- view and run code (since everything is code!),")
    total = 0  # @inspect total
    for x in [1, 2, 3]:  # @inspect x
        total += x  # @inspect total


def difference_between_llm_rl_and_agentic_rl():
    text("## From LLM RL to Agentic RL")
    image("images/agentic/llm-rl-to-agentic.jpg", width=800, center=True)
    text("- Reward design")
    text("- Transition")
    text("- Action space")
    text("- Objective")
    text("- RL Algorithms")
    text("- Environments")
    
    text("## Markov Decision Processes")
    text("PBRFT. The RL training process of preference-based Reinforcement fine-tuning (PBRFT) is formalized as a degenerate MDP defined by the tuple:")
    text(r"$$\langle S_{\text{trad}}, A_{\text{trad}}, P_{\text{trad}}, R_{\text{trad}}, T = 1 \rangle$$", rendering_type="mathjax")
    text("Agentic RL. The RL training process of agentic RL is modeled as a partially observable Markov decision process (POMDP):")
    text(r"$$\left\langle S_{\text{agent}}, A_{\text{agent}}, P_{\text{agent}}, R_{\text{agent}}, \gamma, O \right\rangle$$", rendering_type="mathjax")
    image("images/agentic/comp_pbrft_and_agenticrl.jpg", width=800, center=True)
    
    text("## Training Process")
    text("For PBRFT:")
    text("Text as input -> LLM generates multiple outputs -> human feedback -> Using PPO or DPO to RFT the LLM")
    text("For Agentic RL:")
    text("Observations as input -> Agent choose actions -> Environment returns new observations and rewards -> policy updates")
    image("images/agentic/dpo.jpg", width=400, center=True)
    image("images/agentic/react_rl.jpg", width=400, center=True)
    
    text("## Environment")
    image("images/agentic/agentic_environment.jpg", width=800, center=True)
    text("An example of TextWorld environment:"), link(arxiv_reference("https://arxiv.org/pdf/2010.03768"))
    image("images/agentic/alfworld.png", width=800, center=True)
    
    text("## Action Space")
    text("VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use"), link(arxiv_reference("https://arxiv.org/abs/2509.01055v1"))
    image("images/agentic/verltool.jpg", width=800, center=True)
    
    text("## Transition Dynamics")
    image("images/agentic/transition_dynamics.jpg", width=800, center=True)
    
    text("## Learning Objective")
    image("images/agentic/learning_objective.jpg", width=800, center=True)
    
    text("## RL Algorithms")
    text("- REINFORCE&nbsp;"), link(title="the Policy Gradient Theorem", url="https://huggingface.co/learn/deep-rl-course/unit4/pg-theorem")

    text(r"$$J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}[R(\tau)]$$", rendering_type="mathjax")
    text(r"$$\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \left( \sum_{t=0}^{T} \nabla_\theta \log \pi_\theta(a_t|s_t) \right) \left( \sum_{t=0}^{T} r(s_t, a_t) \right) \right]$$", rendering_type="mathjax")
    
    text("- Proximal Policy Optimization (PPO)"), link(arxiv_reference("https://arxiv.org/abs/1707.06347"))
    
    text(r"$$r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{old}}(a_t|s_t)}$$", rendering_type="mathjax")
    text(r"$$L^{CLIP}(\theta) = \hat{\mathbb{E}}_t \left[ \min \left( r_t(\theta) \hat{A}_t, \text{clip}(r_t(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A}_t \right) \right]$$", rendering_type="mathjax")
    
    text("- Direct Preference Optimization (DPO)"), link(arxiv_reference("https://arxiv.org/abs/2305.18290"))
    
    text(r"$$L_{DPO}(\pi_\theta; \pi_{ref}) = - \mathbb{E}_{(x, y_w, y_l) \sim D} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)} \right) \right]$$", rendering_type="mathjax")
    
    text("- Group Relative Policy Optimization (GRPO)"), link(arxiv_reference("https://arxiv.org/abs/2402.03300"))
    
    text(r"$$r_{i,t}(\theta) = \frac{\pi_{\theta}(o_{i,t} \mid q, o_{i, \lt t})}{\pi_{\theta_{\mathrm{old}}}(o_{i,t} \mid q, o_{i, \lt t})}$$", rendering_type="mathjax")
    text(r"$$L_{i,t}(\theta) = \min \left( r_{i,t}(\theta) \hat{A}_{i,t}, \operatorname{clip}(r_{i,t}(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A}_{i,t} \right)$$", rendering_type="mathjax")
    text(r"$$J_{\text{GRPO}}(\theta) = \mathbb{E}_{q, \{o_i\}} \left[ \frac{1}{G} \sum_{i=1}^{G} \sum_{t=0}^{|o_i|-1} L_{i,t}(\theta) \right]$$", rendering_type="mathjax")
    
    image("images/agentic/variants_of_rl.jpg", width=800, center=True)
    

def capability_perspective():
    image("images/agentic/model_capability.jpg", width=800, center=True)
    text("LLM Agent = LLM + Reasoning + Planning + Memory + Perception + Tool Use + Self-Improve")
    text("---")
    
    text("## Capabilities")
    image("images/agentic/agentic_aspects.jpg", width=800, center=True)
    
    rl_for_reasoning_perception()
    rl_for_planning()
    rl_for_tool_use()
    rl_for_agent_memory()
    rl_for_self_improvement()


def rl_for_reasoning_perception():
    text("### Reasoning")
    text("- OpenAI's o3 "), link("https://openai.com/index/openai-o3-mini/")
    text("- DeepSeek's r1"), link(arxiv_reference("https://arxiv.org/pdf/2501.12948.pdf"))
    text("### Perception")
    text("**image**")
    text("- DeepEyes"), link(arxiv_reference("https://arxiv.org/abs/2505.14362"))
    text("**video**")
    text("- Video-R1"), link(arxiv_reference("https://arxiv.org/abs/2503.21776"))
    text("**audio**")
    text("- EchoInk-R1"), link(arxiv_reference("https://arxiv.org/abs/2505.04623"))
    

def rl_for_planning():
    text("### RL as external driver")
    text("Reasoning with Language Model is Planning with World Model"), link(arxiv_reference("https://arxiv.org/abs/2305.14992"))
    image("images/agentic/rl_as_external_guide.jpg", width=800, center=True)
    link(title="MCT Demo", url="https://github.com/maitrix-org/llm-reasoners/blob/main/demo.ipynb")
    text("### RL as internal driver")
    text("Encouraging Good Processes Without the Need for Good Answers"), link(arxiv_reference("https://arxiv.org/abs/2508.19598", organization="Tencent"))
    image("images/agentic/rl_as_internal_guide.jpg", width=800, center=True)
    text(r"$$R_{total} = \begin{cases}-1, & \text{if trajectory format is invalid}, \\ R_{comp} + R_{rule}, & \text{otherwise}. \end{cases}$$", rendering_type="mathjax")
    text("where $R_{comp}$ is the tooluse completeness reward, $R_{rule}$ is the rule based reward including a negative repetition reward Rrepeat to discourage redundant tool calls, and a negative reward Rerror as a penalty for incorrect tool usage. ")
    

def rl_for_tool_use():
    image("images/agentic/agent_tool_use.jpg", width=800, center=True)
    
    text("### ReAct-style Tool Calling")
    text("Leverages 1)Prompt Engineering or 2)SFT-based methods to enable LLMs to follow the 'Observation-Thinking-Action' tool-use behaviors.")
    text("AgentBank"), link(arxiv_reference("https://arxiv.org/abs/2410.07706"))
    image("images/agentic/agent_bank.jpg", width=800, center=True)
    
    text("### Tool-integrated RL")
    text("Enables agents to strategically decide when, how, and in what combination to invoke tools")
    text("OpenAI o3 o4 DeepResearch&nbsp;"), link(title="Introducing deep research", url="https://openai.com/index/introducing-deep-research/")
    text("UI-TARS-2"), link(arxiv_reference("https://arxiv.org/abs/2509.02544"))
    link(title="UI-TARS-2 DEMO", url="https://seed-tars.com/showcase/ui-tars-2/")
    image("images/agentic/UI-TARS-2.jpg", width=800, center=True)
    
    text("### Long-horizon RL")
    text("Current RL approaches often depend on outcome-based rewards, making it difficult to pinpoint which specific tool invocation in a long, interdependent sequence contributed to success or failure.")
    text("step-level advantage estimation in SpaRL"), link(arxiv_reference("https://arxiv.org/abs/2505.20732"))
    image("images/agentic/SpaRL.jpg", width=800, center=True)
    
    
def rl_for_agent_memory():
    image("images/agentic/rl_for_memory_overview.jpg", width=800, center=True)
    text("### RAG-style")
    text("MemoryBank"), link(arxiv_reference("https://arxiv.org/abs/2305.10250"))
    image("images/agentic/memory_bank.jpg", width=800, center=True)
    text("Memory-R1"), link(arxiv_reference("https://arxiv.org/abs/2508.19828"))
    image("images/agentic/memory-r1.jpg", width=800, center=True)
    image("images/agentic/overview-of-memory-r1.jpg", width=800, center=True)
    
    text("### RL for Token-level Memory")
    text("MemAgent"), link(arxiv_reference("https://arxiv.org/abs/2507.02259", organization="ByteDance"))
    image("images/agentic/mem_agent.jpg", width=800, center=True)
    text("ReSum"), link(arxiv_reference("https://arxiv.org/abs/2509.13313", organization="Alibaba"))
    image("images/agentic/resum.jpg", width=800, center=True)
    text("**example for qwen deepresearch:**")
    image("images/agentic/qwen_deep_research.jpg", width=800, center=True)
    link(title="基于大语言模型的代理强化学习（Agentic RL）深度研究报告.pdf", url="var/files/基于大语言模型的代理强化学习（Agentic RL）深度研究报告.pdf")
    

def rl_for_self_improvement():
    text("- RL for Verbal Self-correction.")
    text("- RL for Internalizing Self-correction.")
    text("- RL for Iterative Self-training.")
    text("---")
    text("### RL for Verbal Self-correction")
    text("Utilizing prompt engineering/rl base methods.")
    text("Agents generate an answer, linguistically reflect on its potential errors, and subsequently produce a refined solution.")
    text("### RL for Internalizing Self-correction")
    text("ACC-Collab"), link(arxiv_reference("https://arxiv.org/abs/2411.00053"))
    image("images/agentic/actor_critic.jpg", width=800, center=True)
    text("### RL for Iterative Self-training")
    text("Absolute Zero"), link(arxiv_reference("https://arxiv.org/abs/2505.03335"))
    image("images/agentic/absolute_zero.jpg", width=800, center=True)
    text("Learning Different Modes of Reasoning:")
    text("Deduction(演绎): predicting the output o given a program p and input i, capturing step-by-step logical reasoning.")
    text("Abduction(溯因): inferring a plausible input i given the program p and an output o, resembling trial-and-error or online search.")
    text("Induction(归纳): synthesizing a program p from a set of in-out examples, requiring generalization from partial information")
    
    text("MAPoRL"), link(arxiv_reference("https://arxiv.org/abs/2502.18439"))
    image("images/agentic/maporl.jpg", width=800, center=True)
    image("images/agentic/maporl_demo.jpg", width=800, center=True)
    

def vertical_domains():
    image("images/agentic/vertical_domains.jpg", width=800, center=True)


def rstar2_agent():
    text("rStar2-Agent: Agentic Reasoning Technical Report"), link(rstar_agent)
    text("## Overview")
    text("Based on Qwen3-14B trained with agentic reinforcement learning to achieve frontier-level performance")
    image("images/agentic/rstar2_bench.png", width=600, center=True)
    text("### An example")
    text("Agent can use Python coding tools and reflect on code execution feedback")
    image("images/agentic/rstar2_demo.png", width=800, center=True)
    text("full information:"), link("https://yuque.antfin.com/vihe9q/oeo4yp/dfunmnxdwq8gxbyn")