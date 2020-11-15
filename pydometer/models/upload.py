from pydometer.models.user import User
from pydometer.models.trial import Trial
from shutil import copyfile

class Upload:

    upload_directory = 'public/uploads'

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
            self.file_path = Upload.generate_file_path(user, trial)
        else:
            raise ValueError("A file path or user and trial parameters must be provided.")

    def create(self, temp_file, user_params, trial_params):
        upload = Upload(user_params=user_params, trial_params=trial_params)
        copyfile(temp_file, upload.file_path)
        return upload

    def find(file_path):
        pass
        #TODO: self.new(file_path)

    def all():
        pass
        #TODO:
        # file_paths = Dir.glob(File.join(UPLOAD_DIRECTORY, "*"))
        # file_paths.map { |file_path| self.new(file_path) }

    def generate_file_path(self, user, trial):
        pass
        #TODO:
        # UPLOAD_DIRECTORY +
        # "#{user.gender}-#{user.height}-#{user.stride}_" +
        # "#{trial.name}-#{trial.rate}-#{trial.steps}.txt"
