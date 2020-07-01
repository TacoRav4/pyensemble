# bio_params.py
# global parameters for all of the musmemfmri bio pilot experiments 
#### make sure the name of each dictionary matches the name of the experiment in pyensemble! 
#that's how it pics the right ones...

#07nnc01171 - error on last recall trial
#10jso99021 = error after 40 expo trials
#10zoc94141 - error after 17 recall trials 
#03mil97181 - error after 40 expo trials
#05wrd01241 - error after 40 expo trials

#11dra01011 - error on last recall trial?!

#01haf01111 = error after 40 expo trials
#05rsj00211 - error after 17 recall trials (ACTUALLY: he seems to have done the study 2x?s)


#12lrm98131 - keeping in, but had a weird glith during expo practice where the first recall response was
#logged to form 6 (person_attention_practice)...

#08eam00311 - something weird happened here. e.g. 
#-look at these reponses in expo task: 23202-23203 (same trial recall (27) submitted 2xs?! )
#-look at these reponses in recall task: 23519-23525

#11mem98201 - also repeat expo response? this time extra attrictive response, says they saw M1_asian_chinese during practice? id: 24289

#03jgj99271 - for some reason just never got the hearing form and skipped right to the PANAS

#on last day, now 2 particpants who can't get past the script that assigns face-trials 

def bio_params():
    study_params = {
        #params for the first bio pilot study
        'musmemfmri_bio_pilot': {
            'experiment_id': 1,
            'ignore_subs': ['01mtt01011','01mtt89011','01ttf67012','04ttt89211','04ktb89211','01mtt89012','01ttt89011',
                            '01ttt89011','02weh90191','01mtt90011','01mtt91011','01ttt69011','02wem90191','04ktb20211',
                            '01ttt72011','04ttt80211','04ttt99211','01ttt44011','01ttt72012','01ttt89012','10zoc94141',
                            '06asm20041','07coa00241','07oal99251','09hsr97191','11eia97261','11kyp96161','11tod99211',
                            '01gah01011','01vlm00061','03jis99161','03tss91111','05yuk98101','01ttt30071','10jso99021',
                            '06pae00241','06snr00011','07hom01111','07prj92121','01tyt79011','07nnc01171','03mil97181',
                            '05wrd01241','11dra01011','01haf01111','05rsj00211','08eam00311','11mem98201'],#07coa00241','06asm20041',
            'breakAfterTheseTrials': ['trial10','trial20','trial30'],
            'practice_face_stim_ids': [840, 841],
            'face_stim_ids': [range(820,820+20)],
            'encoding_bio_duration_ms': 16000,#16000
            'encoding_bio_feedback_duration_ms': 8000,
            'encoding_1back_question_duration_ms': 8000,
            'encoding_rest_duration_ms': 10000,
            'encoding_trials_1-20': range(146,146+20),
            'encoding_trials_21-40': range(166,166+20),
            'bioFeature_names': ['face_name','location','job','hobby','relation','relation_name'],
            'bio_template': ['Hi, my name is [insert_face_name]. ' +
                    'I live in [insert_location] and work as a [insert_job]. ' +
                    'I enjoy [insert_hobby] in my spare time with my [insert_relation] [insert_relation_name].'],
            'form_names': ['post_bio_q2_face_name','post_bio_q2_location','post_bio_q2_job',
                    'post_bio_q2_hobby','post_bio_q2_relation','post_bio_q2_relation_name'],
            'data_dump_path': '/home/bmk/musmemfmri/bio_pilot_data',
            'alt_feature_answers': {'grandmother':'grandma','mom':'mother','dad':'father','grandfather':'grandpa'}
        },
        #this exp same as above, except feedback is given after each face-bio exposure trial 
        'musmemfmri_bio_pilotV2': {
            'experiment_id': '???',
            'ignore_subs': ['',''],
            'breakAfterTheseTrials': ['trial10','trial20','trial30'],
            'practice_face_stim_ids': [840, 841],
            'face_stim_ids': [range(820,820+20)],
            'encoding_bio_duration_ms': 16000,#16000
            'encoding_bio_feedback_duration_ms': 8000,
            'encoding_1back_question_duration_ms': 8000,
            'encoding_rest_duration_ms': 10000,
            'encoding_trials_1-20': range(146,146+20),
            'encoding_trials_21-40': range(166,166+20),
            'bioFeature_names': ['face_name','location','job','hobby','relation','relation_name'],
            'bio_template': ['Hi, my name is [insert_face_name]. ' +
                    'I live in [insert_location] and work as a [insert_job]. ' +
                    'I enjoy [insert_hobby] in my spare time with my [insert_relation] [insert_relation_name].'],
            'form_names': ['post_bio_q2_face_name','post_bio_q2_location','post_bio_q2_job',
                    'post_bio_q2_hobby','post_bio_q2_relation','post_bio_q2_relation_name'],
            'data_dump_path': '/home/bmk/musmemfmri/bio_pilotV2_data',
            'alt_feature_answers': {'grandmother':'grandma','mom':'mother','dad':'father','grandfather':'grandpa'}
        }
    }

    return study_params




