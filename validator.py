def validate_workflow(nodes):

    errors = []

    if "Start" not in nodes:
        errors.append("Missing Start Node")

    if "End" not in nodes:
        errors.append("Missing End Node")

    return errors