# Final Project in Deep Learning Course at Ben Gurion University

Stav Dratva & Peleg Eliyahou (Group 3)

This repository contains code to reproduce the results of Enhancing Question Classification with Augmented Data project.

### Installing Requirements

In order to run the code, you should make sure the libraries requirements are satisfied.
Install the requirements using pip

```bash
pip install -r requirements.txt
```


## Running the Experiments

To run the experiments, you can use the following command:

```bash
python main.py TREC BERT --learning_rate=5e-5 --batch_size=128 --num_train_epochs=10 > output.txt
```


### Data Augmentation 

For your convenience, we added the data directories after performing the data augmentation so you don't must to perform the following steps.
In order to run the experiments with the augmented data files we attached, you should copy the relevant data directory, change its name to "data" and place it instead of the "data" directory.

If you want to run yourself the code to produce the data augmentation files, you should run the following Python files from the "data_augmentation" directory:

1. *augment.py* - The code that produces the EDA augmented files. You should change the following parameters in the "arguments" dictionary:
   num_aug = The number of augmented sentences that will produce from each original record.
   output_clean, output, output_labels = The file path of the output files.
2. *backtranslation.py* - The code that performs back translation to Hebrew from the original dataset.
   The chosen target language for this experiment was Hebrew. If you want to perform back translation to another language you can change the value of "target_lang" in the "arguments" dictionary.
3. *eda+backtranslation.py* - The code that performs back translation to Hebrew from the augmented EDA files. You can change the EDA files you want to perform back translation on by changing the "input" arguments in the "arguments" dictionary.

The available languages for back translation are as follows:
   - af - afrikaans
   - sq - albanian
   - am - amharic
   - ar - arabic
   - hy - armenian
   - az - azerbaijani
   - eu - basque
   - be - belarusian
   - bn - bengali
   - bs - bosnian
   - bg - bulgarian
   - ca - catalan
   - ceb - cebuano
   - ny - chichewa
   - zh-cn - chinese (simplified)
   - zh-tw - chinese (traditional)
   - co - corsican
   - hr - croatian
   - cs - czech
   - da - danish
   - nl - dutch
   - en - english
   - eo - esperanto
   - et - estonian
   - tl - filipino
   - fi - finnish
   - fr - french
   - fy - frisian
   - gl - galician
   - ka - georgian
   - de - german
   - el - greek
   - gu - gujarati
   - ht - haitian creole
   - ha - hausa
   - haw - hawaiian
   - iw - hebrew
   - hi - hindi
   - hmn - hmong
   - hu - hungarian
   - is - icelandic
   - ig - igbo
   - id - indonesian
   - ga - irish
   - it - italian
   - ja - japanese
   - jw - javanese
   - kn - kannada
   - kk - kazakh
   - km - khmer
   - ko - korean
   - ku - kurdish (kurmanji)
   - ky - kyrgyz
   - lo - lao
   - la - latin
   - lv - latvian
   - lt - lithuanian
   - lb - luxembourgish
   - mk - macedonian
   - mg - malagasy
   - ms - malay
   - ml - malayalam
   - mt - maltese
   - mi - maori
   - mr - marathi
   - mn - mongolian
   - my - myanmar (burmese)
   - ne - nepali
   - no - norwegian
   - or - odia
   - ps - pashto
   - fa - persian
   - pl - polish
   - pt - portuguese
   - pa - punjabi
   - ro - romanian
   - ru - russian
   - sm - samoan
   - gd - scots gaelic
   - sr - serbian
   - st - sesotho
   - sn - shona
   - sd - sindhi
   - si - sinhala
   - sk - slovak
   - sl - slovenian
   - so - somali
   - es - spanish
   - su - sundanese
   - sw - swahili
   - sv - swedish
   - tg - tajik
   - ta - tamil
   - te - telugu
   - th - thai
   - tr - turkish
   - uk - ukrainian
   - ur - urdu
   - ug - uyghur
   - uz - uzbek
   - vi - vietnamese
   - cy - welsh
   - xh - xhosa
   - yi - yiddish
   - yo - yoruba
   - zu - zulu

After producing the data augmentation files, the augmented files will appear in the "data_augmentation" directory.
The data augmentation code creates three text files, their key names in the "arguments" dictionary are as follows. You should change the names of the files and place them as described:
1. *output* - This argument is the path that will produce the data file that should be placed in the following path instead of the file there: corpus/TREC.txt
2. *output_clean* -  This argument is the path that will produce the data file that should be placed in the following path instead of the file there: corpus/TREC.clean.txt
3. *output_labels* -  This argument is the path that will produce the data file that should be placed in the following path instead of the file there: data/TREC/TREC.txt


## Results
In the file "output.txt" you will see the evaluation results of the training sets over the different epochs.
In the file output\eval_results.json you will see the evaluation results of the test set.


## Acknowledgments

Sun, C., Qiu, X., Xu, Y., & Huang, X. (2019). How to fine-tune bert for text classification?. In Chinese Computational Linguistics: 18th China National Conference, CCL 2019, Kunming, China, October 18–20, 2019, Proceedings 18 (pp. 194-206). Springer International Publishing.‏

Wei, J., & Zou, K. (2019). Eda: Easy data augmentation techniques for boosting performance on text classification tasks. arXiv preprint arXiv:1901.11196.‏


