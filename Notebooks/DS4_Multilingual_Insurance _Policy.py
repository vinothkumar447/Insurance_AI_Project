{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "43d76108-c342-47cc-8eaa-e9dd650c56eb",
   "metadata": {},
   "source": [
    "# **<div style=\"text-align: center; color: black; font-size: 30px;\">Multilingual Insurance Policy </div>**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1709c95-f677-4194-bd05-18c38a83e41c",
   "metadata": {},
   "source": [
    "#### Import the Library"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b4ffc927-ace9-415c-a619-b8bc7053c426",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import random\n",
    "from faker import Faker"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7144c991-a453-47ee-8949-b94c14be6b44",
   "metadata": {},
   "source": [
    "#### Create Synthetic Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "47525e99-9781-407f-942e-8c2df163786a",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# Initialize Faker for different languages\n",
    "fake_en = Faker(\"en_US\")\n",
    "fake_fr = Faker(\"fr_FR\")\n",
    "fake_es = Faker(\"es_ES\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9ec3b1d1-8258-40e9-874c-1b7549272d60",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate synthetic data\n",
    "data = []\n",
    "for _ in range(5000):\n",
    "    policy_id = f\"POL{random.randint(100000, 999999)}\"\n",
    "    policy_text_en = fake_en.paragraph(nb_sentences=5)\n",
    "    policy_text_fr = fake_fr.paragraph(nb_sentences=5)\n",
    "    policy_text_es = fake_es.paragraph(nb_sentences=5)\n",
    "    summarized_text = fake_en.sentence(nb_words=15)  \n",
    "\n",
    "    data.append([policy_id, policy_text_en, policy_text_fr, policy_text_es, summarized_text])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c3bb3491-1098-46d3-b2a2-92d072d377ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create DataFrame\n",
    "df_policy= pd.DataFrame(data, columns=[\"Policy_ID\", \"Policy_Text_EN\", \"Policy_Text_FR\", \"Policy_Text_ES\", \"Summarized_Text\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e9269bb3-2cdb-40e3-8182-fdff7c411d07",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save dataset as CSV\n",
    "df_policy.to_csv(\"synthetic_policy_data.csv\", index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db45a4a4-28e4-4250-9dfb-43b8086b006c",
   "metadata": {},
   "source": [
    "#### Data Analysis & Inspection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d3a17fe5-404b-4092-9fa9-9c5a10b31c80",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Policy_ID</th>\n",
       "      <th>Policy_Text_EN</th>\n",
       "      <th>Policy_Text_FR</th>\n",
       "      <th>Policy_Text_ES</th>\n",
       "      <th>Summarized_Text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>POL837996</td>\n",
       "      <td>Your few spend thing say stop single worker. M...</td>\n",
       "      <td>Vent tour habitude ministre profond haute sec....</td>\n",
       "      <td>Assumenda cum libero eaque. Nam labore adipisc...</td>\n",
       "      <td>Ever defense according off military according ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>POL569442</td>\n",
       "      <td>Forget former task news. Court if picture morn...</td>\n",
       "      <td>Humide arrière bord bien certain toile. Descen...</td>\n",
       "      <td>In a temporibus. Quam officia consequatur exer...</td>\n",
       "      <td>Information however surface read build nationa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>POL401158</td>\n",
       "      <td>Oil bad add including tree state forget war. C...</td>\n",
       "      <td>Effacer savoir troisième jeu. Refuser calme do...</td>\n",
       "      <td>Ad maxime aliquam dicta doloribus quibusdam. C...</td>\n",
       "      <td>Time kid indicate when address many road cultu...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>POL858952</td>\n",
       "      <td>Financial you hope front. Hope worry history t...</td>\n",
       "      <td>Sous demain haut terre refuser reposer posséde...</td>\n",
       "      <td>Hic laudantium esse. Ducimus occaecati facere ...</td>\n",
       "      <td>Evidence garden air amount after Congress scie...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>POL887724</td>\n",
       "      <td>Ten beat lead future. Why figure television ta...</td>\n",
       "      <td>Vêtir recherche joli pauvre. Retrouver tracer ...</td>\n",
       "      <td>Quaerat tenetur non ullam sint. Delectus numqu...</td>\n",
       "      <td>Back clear memory bad in next over since sort ...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Policy_ID                                     Policy_Text_EN  \\\n",
       "0  POL837996  Your few spend thing say stop single worker. M...   \n",
       "1  POL569442  Forget former task news. Court if picture morn...   \n",
       "2  POL401158  Oil bad add including tree state forget war. C...   \n",
       "3  POL858952  Financial you hope front. Hope worry history t...   \n",
       "4  POL887724  Ten beat lead future. Why figure television ta...   \n",
       "\n",
       "                                      Policy_Text_FR  \\\n",
       "0  Vent tour habitude ministre profond haute sec....   \n",
       "1  Humide arrière bord bien certain toile. Descen...   \n",
       "2  Effacer savoir troisième jeu. Refuser calme do...   \n",
       "3  Sous demain haut terre refuser reposer posséde...   \n",
       "4  Vêtir recherche joli pauvre. Retrouver tracer ...   \n",
       "\n",
       "                                      Policy_Text_ES  \\\n",
       "0  Assumenda cum libero eaque. Nam labore adipisc...   \n",
       "1  In a temporibus. Quam officia consequatur exer...   \n",
       "2  Ad maxime aliquam dicta doloribus quibusdam. C...   \n",
       "3  Hic laudantium esse. Ducimus occaecati facere ...   \n",
       "4  Quaerat tenetur non ullam sint. Delectus numqu...   \n",
       "\n",
       "                                     Summarized_Text  \n",
       "0  Ever defense according off military according ...  \n",
       "1  Information however surface read build nationa...  \n",
       "2  Time kid indicate when address many road cultu...  \n",
       "3  Evidence garden air amount after Congress scie...  \n",
       "4  Back clear memory bad in next over since sort ...  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# printing the first 5 rows of the dataframe\n",
    "df_policy.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "79b8432a-8970-4446-99c3-1767f0698453",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5000, 5)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# number of rows and columns in the data frame\n",
    "df_policy.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6ffefde8-0aae-41f2-9e3d-a3232e076c00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 5000 entries, 0 to 4999\n",
      "Data columns (total 5 columns):\n",
      " #   Column           Non-Null Count  Dtype \n",
      "---  ------           --------------  ----- \n",
      " 0   Policy_ID        5000 non-null   object\n",
      " 1   Policy_Text_EN   5000 non-null   object\n",
      " 2   Policy_Text_FR   5000 non-null   object\n",
      " 3   Policy_Text_ES   5000 non-null   object\n",
      " 4   Summarized_Text  5000 non-null   object\n",
      "dtypes: object(5)\n",
      "memory usage: 195.4+ KB\n"
     ]
    }
   ],
   "source": [
    "# getting more information about the dataset\n",
    "df_policy.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a0913e52-d16e-434e-baad-c0a1db9fb07d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Policy_ID          0\n",
       "Policy_Text_EN     0\n",
       "Policy_Text_FR     0\n",
       "Policy_Text_ES     0\n",
       "Summarized_Text    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# checking the missing values in each column\n",
    "df_policy.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6dd59eca-e6eb-4734-b471-b02ab3c48166",
   "metadata": {},
   "source": [
    "#### Data Pre-ProcessingData Pre-Processing"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "50eb37db-e1de-4727-a6c0-20a04ce502e9",
   "metadata": {},
   "source": [
    "##### Text Normalization "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "5c0c64ec-9814-4f0c-87d3-89a6ade48b8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "import contractions\n",
    "\n",
    "def normalize_text(text):\n",
    "    if pd.isna(text):\n",
    "        return \"\"\n",
    "    text = text.lower()  # Convert to lowercase\n",
    "    text = contractions.fix(text)  # Expand contractions\n",
    "    text = re.sub(r'[^a-zA-Z0-9\\s]', '', text)  # Remove special characters\n",
    "    text = re.sub(r'\\s+', ' ', text).strip()  # Remove extra spaces\n",
    "    return text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "d58c7028-5062-4611-b451-5b198042d4f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "df_policy['Policy_Text_EN'] = df_policy['Policy_Text_EN'].apply(normalize_text)\n",
    "df_policy['Policy_Text_FR'] = df_policy['Policy_Text_FR'].apply(normalize_text)\n",
    "df_policy['Policy_Text_ES'] = df_policy['Policy_Text_ES'].apply(normalize_text)\n",
    "df_policy['Summarized_Text'] = df_policy['Summarized_Text'].apply(normalize_text)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c4b97454-2620-40e3-93b6-3727f5e682f6",
   "metadata": {},
   "source": [
    "#### Tokenization & Embeddings "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c53c8fb2-b249-4d65-b728-c3a4f2a16a1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tokenizers import Tokenizer, models, pre_tokenizers, trainers, processors\n",
    "\n",
    "# Initialize a BPE tokenizer\n",
    "bpe_tokenizer = Tokenizer(models.BPE())\n",
    "\n",
    "# Initialize a WordPiece tokenizer\n",
    "wordpiece_tokenizer = Tokenizer(models.WordPiece(unk_token=\"[UNK]\"))\n",
    "\n",
    "# Pre-tokenization (splitting text into words)\n",
    "bpe_tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()\n",
    "wordpiece_tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "daf7736e-50c5-423e-ade0-3de8a61b0ca6",
   "metadata": {},
   "source": [
    "#### Parallel Corpus Alignment "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "c08cbece-c69e-444c-8df1-ea762b065d4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-02-24 12:39:10,688 - simalign.simalign - INFO - Initialized the EmbeddingLoader with model: bert-base-multilingual-cased\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[21], line 7\u001b[0m\n\u001b[0;32m      4\u001b[0m aligner \u001b[38;5;241m=\u001b[39m SentenceAligner(model\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mbert\u001b[39m\u001b[38;5;124m\"\u001b[39m, token_type\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mbpe\u001b[39m\u001b[38;5;124m\"\u001b[39m, matching_methods\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmai\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      6\u001b[0m \u001b[38;5;66;03m# Perform sentence alignment between English and French policies\u001b[39;00m\n\u001b[1;32m----> 7\u001b[0m alignment_en_fr \u001b[38;5;241m=\u001b[39m aligner\u001b[38;5;241m.\u001b[39mget_word_aligns(df_policy[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPolicy_Text_EN\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mtolist(), df_policy[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPolicy_Text_FR\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mtolist())\n\u001b[0;32m      9\u001b[0m \u001b[38;5;66;03m# Perform sentence alignment between English and Spanish policies\u001b[39;00m\n\u001b[0;32m     10\u001b[0m alignment_en_es \u001b[38;5;241m=\u001b[39m aligner\u001b[38;5;241m.\u001b[39mget_word_aligns(df_policy[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPolicy_Text_EN\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mtolist(), df_policy[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPolicy_Text_ES\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mtolist())\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\simalign\\simalign.py:222\u001b[0m, in \u001b[0;36mSentenceAligner.get_word_aligns\u001b[1;34m(self, src_sent, trg_sent)\u001b[0m\n\u001b[0;32m    220\u001b[0m all_mats[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124minter\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m all_mats[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfwd\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m*\u001b[39m all_mats[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mrev\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[0;32m    221\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmwmf\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mmatching_methods:\n\u001b[1;32m--> 222\u001b[0m \tall_mats[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmwmf\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mget_max_weight_match(sim)\n\u001b[0;32m    223\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mitermax\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mmatching_methods:\n\u001b[0;32m    224\u001b[0m \tall_mats[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mitermax\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39miter_max(sim)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\simalign\\simalign.py:102\u001b[0m, in \u001b[0;36mSentenceAligner.get_max_weight_match\u001b[1;34m(sim)\u001b[0m\n\u001b[0;32m    100\u001b[0m \t\t\u001b[38;5;28;01mreturn\u001b[39;00m edge[\u001b[38;5;241m1\u001b[39m], edge[\u001b[38;5;241m0\u001b[39m] \u001b[38;5;241m-\u001b[39m sim\u001b[38;5;241m.\u001b[39mshape[\u001b[38;5;241m0\u001b[39m]\n\u001b[0;32m    101\u001b[0m G \u001b[38;5;241m=\u001b[39m from_biadjacency_matrix(csr_matrix(sim))\n\u001b[1;32m--> 102\u001b[0m matching \u001b[38;5;241m=\u001b[39m nx\u001b[38;5;241m.\u001b[39mmax_weight_matching(G, maxcardinality\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n\u001b[0;32m    103\u001b[0m matching \u001b[38;5;241m=\u001b[39m [permute(x) \u001b[38;5;28;01mfor\u001b[39;00m x \u001b[38;5;129;01min\u001b[39;00m matching]\n\u001b[0;32m    104\u001b[0m matching \u001b[38;5;241m=\u001b[39m \u001b[38;5;28msorted\u001b[39m(matching, key\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mlambda\u001b[39;00m x: x[\u001b[38;5;241m0\u001b[39m])\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\networkx\\utils\\decorators.py:789\u001b[0m, in \u001b[0;36margmap.__call__.<locals>.func\u001b[1;34m(_argmap__wrapper, *args, **kwargs)\u001b[0m\n\u001b[0;32m    788\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mfunc\u001b[39m(\u001b[38;5;241m*\u001b[39margs, __wrapper\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs):\n\u001b[1;32m--> 789\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m argmap\u001b[38;5;241m.\u001b[39m_lazy_compile(__wrapper)(\u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "File \u001b[1;32m<class 'networkx.utils.decorators.argmap'> compilation 18:5\u001b[0m, in \u001b[0;36margmap_max_weight_matching_13\u001b[1;34m(G, maxcardinality, weight, backend, **backend_kwargs)\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mgzip\u001b[39;00m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01minspect\u001b[39;00m\n\u001b[1;32m----> 5\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mitertools\u001b[39;00m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mre\u001b[39;00m\n\u001b[0;32m      7\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mwarnings\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\networkx\\utils\\backends.py:633\u001b[0m, in \u001b[0;36m_dispatchable.__call__\u001b[1;34m(self, backend, *args, **kwargs)\u001b[0m\n\u001b[0;32m    628\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"Returns the result of the original function, or the backend function if\u001b[39;00m\n\u001b[0;32m    629\u001b[0m \u001b[38;5;124;03mthe backend is specified and that backend implements `func`.\"\"\"\u001b[39;00m\n\u001b[0;32m    631\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m backends:\n\u001b[0;32m    632\u001b[0m     \u001b[38;5;66;03m# Fast path if no backends are installed\u001b[39;00m\n\u001b[1;32m--> 633\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39morig_func(\u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n\u001b[0;32m    635\u001b[0m \u001b[38;5;66;03m# Use `backend_name` in this function instead of `backend`\u001b[39;00m\n\u001b[0;32m    636\u001b[0m backend_name \u001b[38;5;241m=\u001b[39m backend\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\networkx\\algorithms\\matching.py:986\u001b[0m, in \u001b[0;36mmax_weight_matching\u001b[1;34m(G, maxcardinality, weight)\u001b[0m\n\u001b[0;32m    984\u001b[0m     \u001b[38;5;28;01mcontinue\u001b[39;00m\n\u001b[0;32m    985\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m (v, w) \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m allowedge:\n\u001b[1;32m--> 986\u001b[0m     kslack \u001b[38;5;241m=\u001b[39m slack(v, w)\n\u001b[0;32m    987\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m kslack \u001b[38;5;241m<\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;241m0\u001b[39m:\n\u001b[0;32m    988\u001b[0m         \u001b[38;5;66;03m# edge k has zero slack => it is allowable\u001b[39;00m\n\u001b[0;32m    989\u001b[0m         allowedge[(v, w)] \u001b[38;5;241m=\u001b[39m allowedge[(w, v)] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mTrue\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\networkx\\algorithms\\matching.py:512\u001b[0m, in \u001b[0;36mmax_weight_matching.<locals>.slack\u001b[1;34m(v, w)\u001b[0m\n\u001b[0;32m    511\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mslack\u001b[39m(v, w):\n\u001b[1;32m--> 512\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m dualvar[v] \u001b[38;5;241m+\u001b[39m dualvar[w] \u001b[38;5;241m-\u001b[39m \u001b[38;5;241m2\u001b[39m \u001b[38;5;241m*\u001b[39m G[v][w]\u001b[38;5;241m.\u001b[39mget(weight, \u001b[38;5;241m1\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\networkx\\classes\\graph.py:515\u001b[0m, in \u001b[0;36mGraph.__getitem__\u001b[1;34m(self, n)\u001b[0m\n\u001b[0;32m    491\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21m__getitem__\u001b[39m(\u001b[38;5;28mself\u001b[39m, n):\n\u001b[0;32m    492\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Returns a dict of neighbors of node n.  Use: 'G[n]'.\u001b[39;00m\n\u001b[0;32m    493\u001b[0m \n\u001b[0;32m    494\u001b[0m \u001b[38;5;124;03m    Parameters\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    513\u001b[0m \u001b[38;5;124;03m    AtlasView({1: {}})\u001b[39;00m\n\u001b[0;32m    514\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[1;32m--> 515\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39madj[n]\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\networkx\\classes\\coreviews.py:81\u001b[0m, in \u001b[0;36mAdjacencyView.__getitem__\u001b[1;34m(self, name)\u001b[0m\n\u001b[0;32m     80\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21m__getitem__\u001b[39m(\u001b[38;5;28mself\u001b[39m, name):\n\u001b[1;32m---> 81\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m AtlasView(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_atlas[name])\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\networkx\\classes\\coreviews.py:43\u001b[0m, in \u001b[0;36mAtlasView.__init__\u001b[1;34m(self, d)\u001b[0m\n\u001b[0;32m     40\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21m__setstate__\u001b[39m(\u001b[38;5;28mself\u001b[39m, state):\n\u001b[0;32m     41\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_atlas \u001b[38;5;241m=\u001b[39m state[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m_atlas\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[1;32m---> 43\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21m__init__\u001b[39m(\u001b[38;5;28mself\u001b[39m, d):\n\u001b[0;32m     44\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_atlas \u001b[38;5;241m=\u001b[39m d\n\u001b[0;32m     46\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21m__len__\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "from simalign import SentenceAligner\n",
    "\n",
    "# Initialize the sentence aligner with BERT-based embeddings\n",
    "aligner = SentenceAligner(model=\"bert\", token_type=\"bpe\", matching_methods=\"mai\")\n",
    "\n",
    "# Perform sentence alignment between English and French policies\n",
    "alignment_en_fr = aligner.get_word_aligns(df_policy[\"Policy_Text_EN\"].tolist(), df_policy[\"Policy_Text_FR\"].tolist())\n",
    "\n",
    "# Perform sentence alignment between English and Spanish policies\n",
    "alignment_en_es = aligner.get_word_aligns(df_policy[\"Policy_Text_EN\"].tolist(), df_policy[\"Policy_Text_ES\"].tolist())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0db26a81-4e73-4c82-837b-06a64116bc9b",
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install tf-keras"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4446179a-0a77-468b-8b3d-79b4768ced69",
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install sentencepiece\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b8d715e5-3d9d-4e3d-982d-651d3a217699",
   "metadata": {},
   "source": [
    "#### Model Fine-Tuning "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79a2dc21-4213-4bd6-a2e4-978653b3e23a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import MBartForConditionalGeneration, MBartTokenizer, Trainer, TrainingArguments\n",
    "from datasets import Dataset\n",
    "\n",
    "# Load the tokenizer and model\n",
    "model_name = \"facebook/mbart-large-50\"\n",
    "tokenizer = MBartTokenizer.from_pretrained(model_name)\n",
    "model = MBartForConditionalGeneration.from_pretrained(model_name)\n",
    "\n",
    "# Prepare dataset for fine-tuning\n",
    "def preprocess_function(examples):\n",
    "    inputs = tokenizer(examples[\"Policy_Text_EN\"], truncation=True, padding=\"max_length\", max_length=512)\n",
    "    labels = tokenizer(examples[\"Summarized_Text\"], truncation=True, padding=\"max_length\", max_length=512)\n",
    "    inputs[\"labels\"] = labels[\"input_ids\"]\n",
    "    return inputs\n",
    "\n",
    "dataset = Dataset.from_pandas(df_policy)\n",
    "tokenized_datasets = dataset.map(preprocess_function, batched=True)\n",
    "\n",
    "# Training arguments\n",
    "training_args = TrainingArguments(\n",
    "    output_dir=\"./mbart_policy_finetuned\",\n",
    "    evaluation_strategy=\"epoch\",\n",
    "    learning_rate=2e-5,\n",
    "    per_device_train_batch_size=4,\n",
    "    per_device_eval_batch_size=4,\n",
    "    num_train_epochs=3,\n",
    "    weight_decay=0.01,\n",
    "    save_total_limit=2,\n",
    "    save_strategy=\"epoch\",\n",
    ")\n",
    "\n",
    "trainer = Trainer(\n",
    "    model=model,\n",
    "    args=training_args,\n",
    "    train_dataset=tokenized_datasets,\n",
    "    eval_dataset=tokenized_datasets,\n",
    ")\n",
    "\n",
    "# Start training\n",
    "trainer.train()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
