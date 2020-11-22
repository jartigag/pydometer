from models.user import User
from models.trial import Trial
from shutil import copyfile
from os import listdir
from os.path import isfile, join

class Upload:

    UPLOAD_DIRECTORY = 'public/uploads/'

    def __init__(self, file_path=None, user_params=None, trial_params=None):
        if file_path:
            #example: file_path = 'test/data/female-167-70_bagwalk1-100-10.txt'
            self.file_path = file_path
            file_name = self.file_path.split('/')[-1].split('.txt')[0].split('_') #example: file_name = ['female-167-70', 'bagwalk1-100-10']
            self.user = User(*file_name[0].split('-'))
            self.trial = Trial(*file_name[-1].split('-'))
        elif user_params and trial_params:
            self.user = User(**user_params)
            self.trial = Trial(**trial_params)
            self.file_path = Upload.generate_file_path(self.user, self.trial)
        else:
            raise ValueError("A file path or user and trial parameters must be provided.")

    def create(temp_file, user_params, trial_params):
        upload = Upload(user_params=user_params, trial_params=trial_params)
        copyfile(temp_file, upload.file_path)
        return upload

    def find(file_path):
        return Upload(file_path)

    def all():
        file_paths = [join(Upload.UPLOAD_DIRECTORY, f) for f in listdir(Upload.UPLOAD_DIRECTORY) if isfile(join(Upload.UPLOAD_DIRECTORY, f))]
        return [Upload(file_path) for file_path in file_paths]

    def generate_file_path(user, trial):
        return f"{Upload.UPLOAD_DIRECTORY}{user.gender}-{user.height}-{user.stride}_{trial.name}-{trial.rate}-{trial.steps}.txt"
