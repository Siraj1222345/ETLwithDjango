

class Dbrouter:

    droute_app_labels = {'Dstudent'}
    sroute_app_labels = {'Sstudent'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.sroute_app_labels:
            return 'default'
        if model._meta.app_label in self.droute_app_labels:
            return 'postgres'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.sroute_app_labels:
            return 'default'
        if model._meta.app_label in self.droute_app_labels:
            return 'postgres'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.sroute_app_labels or
            obj2._meta.app_label in self.sroute_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.sroute_app_labels:
            return db == 'default'
        if app_label in self.droute_app_labels:
            return db == 'postgres'
        return None