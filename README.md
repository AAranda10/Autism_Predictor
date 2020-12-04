# Autism Predictor

### Author: Austin Aranda

## Description: 

The purpose of this project is to develop a model that is able to predict whether a toddler would potentially be diagnosed with Autism. In being able to predict whether a child could potentially have Autism or not, medical providers would be able to more proactively get children the help they need at a younger age. This model could be further developed with more data and feedback from healthcare specialists in the Autism field. 

In addition, I have provided these deliverables:

    1. Visual of Findings
    
    2. Prep.py and MVP_model.py file to recreate my efforts.
    
    3. Presentation with the results of my findings.

## Project Planning

Initial Questions:
- Is there a certain age range where it's easier to detect Autism in a child?
- Is there a variance based on survey scores?
- Does a child's ethnicity or race play a role?
- What questions are better at predicting Autism in a child?


### Hypotheses:

#### 1st Hypothesis

𝐻 0 - There is no difference in survey scores between children with Autism and all children tested

𝐻 a - There is a difference in survey scores between children with Autism and all children tested

#### 2nd Hypothesis

𝐻 0 - A child having Autism is independent of type of having family history of Autism

𝐻 a - A child having Autism is not independent of type of having family history of Autism

#### 3rd Hypothesis

𝐻 0 - Sex of child is independent of child having Austism

𝐻 a - Sex of child is not independent of child having Autism


## Data Dictionary

| Feature | Definition |
| --- | --- |
| a1 | Does your child look at you when you call his/her name? |
| a2 | How easy is it for you to get eye contact with your child?  |
| a3 | Does your child point to indicate that s/he wants something? |
| a4 | oes your child point to share interest with you? |
| a5 | Does your child pretend? |
| a6 | Does your child follow where you’re looking?  |
| a7 | f you or someone else in the family is visibly upset, does your child show signs 
of wan9ng to comfort them? |
| a8 | Would you describe your child’s first words as: |
| a9 | Does your child use simple gestures? |
| a10 | Does your child stare at nothing with no apparent purpose? |
| age_mons | Child's age in months |
| is_male | Sex of the child ( 1: Male, 0: Female) |
| ethnicity | Ethnicity of child, reported by the person who completed survey |
| whocompletedthetest | Individual who completed survey |
| has_jaundice | Whether jaundice was present in child or not |
| has_fam_history | Whether child had family history of Autism or not |

| Target | Definition |
| --- | --- |
| has_asd | If child was diagnosed with autism or not ( 1: Autism Present, 0: Not Present|


## Key Findings

- It appears that question 1, 4, 5, 6, 7, and 9 are the most effective at differentiating a child with asd or not
- Family history does not appear to be an accurate indicator if a child is autistic or not
- This may not be reliable because typically families don't share their personal medical history
- Males are diagnosed with Autism more than females based on the autism rate
- Ethnicity is not as big of a factor as I had originally had anticipated

## Takeaways

- The MVP performed perfectly on the unseen test data without overfitting
- The Random Forest Model is a solid backup if needed as it had an accuracy of 97 percent on unseen data.
- The MVP model would prove useful for medical providers who would like to be able to streamline the pre diagnosis with an online survey using a website or app.
- Using the MVP model, they would be able to prompt the parent of the patient to make an appointment for early intervention.
- In doing so, children will be able to get the care they need much sooner, rather than later.
