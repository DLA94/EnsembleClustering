from validator import Validator
from experiment import Experiment

if __name__=='__main__':
    dataset = 'iris'
    real_or_artificial = 'real-world'
    real_number_of_classes = 3
    are_clusters_fixed = True
    controller = Experiment(dataset=dataset, real_or_artificial=real_or_artificial, real_number_of_classes=real_number_of_classes, are_clusters_fixed=True)
    controller.preprocess()
    Validator(controller.name, controller.numerical, controller.ground_truth, 'SL', are_clusters_fixed).validate_consensus()