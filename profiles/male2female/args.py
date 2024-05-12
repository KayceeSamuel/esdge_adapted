import argparse
argsall = argparse.Namespace(
    testdata_path='/content/drive/MyDrive/esdge/data/test/male',
    ckpt = '/content/drive/MyDrive/esdge/trained_models/male2female/models/model004500.pt', 
    dsepath = '/content/drive/MyDrive/esdge/pretrained_model/256x256_classifier.pt',
    config_path = 'profiles/male2female/male2female.yml',
    t = 500,
    ls =  500.0,
    li = 2.0,
    s1 = 'cosine',
    s2 = 'neg_l2',
    phase = 'test',
    root = 'runs/',
    sample_step= 1,
    batch_size = 20,
    diffusionmodel = 'DDPM',
    down_N = 32,
    seed=1234)