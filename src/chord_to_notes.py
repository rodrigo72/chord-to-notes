from chord_yacc import parser
import traceback


roots = {
    'C': 0,
    'D': 1,
    'E': 2,
    'F': 2.5,
    'G': 3.5,
    'A': 4.5,
    'B': 5.5,
}

scale_templates = dict(
    major={0, 1, 2, 2.5, 3.5, 4.5, 5.5},
    aeolian={0, 1, 1.5, 2.5, 3.5, 4, 5},
    dorian={0, 1, 1.5, 2.5, 3.5, 4.5, 5},
    phrygian={0, 0.5, 1.5, 2.5, 3.5, 4, 5},
    lydian={0, 1, 2, 3, 3.5, 4.5, 5.5},
    lydian_minor={0, 1, 2, 3, 3.5, 4, 5},
    mixolydian={0, 1, 2, 2.5, 3.5, 4.5, 5},
    locrian={0, 0.5, 1.5, 2.5, 3, 4, 5},
    harmonic_minor={0, 1, 1.5, 2.5, 3.5, 4, 5.5},
    melodic_minor_ascending={0, 1, 1.5, 2.5, 3.5, 4.5, 5.5},
    melodic_minor_descending={0, 1, 1.5, 2.5, 3.5, 4, 5},
    minor_blues={0, 1.5, 2.5, 3, 3.5, 5},
    major_blues={0, 1, 1.5, 2, 3.5, 4.5},
    neapolitan_minor={0, 0.5, 1.5, 2.5, 3.5, 4, 5.5},
    neapolitan_major={0, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5},
    whole_half_diminished={0, 1, 1.5, 2.5, 3, 4, 4.5, 5.5},
    half_whole_diminished={0, 0.5, 1.5, 2, 3, 3.5, 4.5, 5},
    enigmatic={0, 0.5, 2, 3, 4, 5, 5.5},
)

notes = {
    0: "C",
    0.5: ["C#", "Db"],
    1: "D",
    1.5: ["D#", "Eb"],
    2: "E",
    2.5: "F",
    3: ["F#", "Gb"],
    3.5: "G",
    4: ["G#", "Ab"],
    4.5: "A",
    5: ["A#", "Bb"],
    5.5: "B"
}

DEBUG = False


def get_pitch_value(pitch) -> float:
    match pitch:
        case "#":
            return 0.5
        case "b":
            return -0.5
        case _:
            return 0


def get_notes_from_quality(root_value, quality) -> list[str]:
    """using twelve-tone equal temperament"""
    match quality:
        case "m":
            minor_third = root_value + 3 * 0.5
            perfect_fifth = root_value + 7 * 0.5
            return [minor_third, perfect_fifth]
        case "M":
            major_third = root_value + 4 * 0.5
            perfect_fifth = root_value + 7 * 0.5
            return [major_third, perfect_fifth]
        case "aug":
            major_third = root_value + 4 * 0.5
            augmented_fifth = root_value + 7 * 0.5 + 0.5
            return [major_third, augmented_fifth]
        case "dim":
            minor_third = root_value + 3 * 0.5
            diminished_fifth = root_value + 7 * 0.5 - 0.5
            return [minor_third, diminished_fifth]
        case "ø":
            minor_third = root_value + 3 * 0.5
            diminished_fifth = root_value + 7 * 0.5 - 0.5
            minor_seventh = root_value + 10 * 0.5
            return [minor_third, diminished_fifth, minor_seventh]
        case _:
            raise ValueError(f"Type of quality not found '{quality}'.")


def get_notes_from_elements(root_value, elements):
    values_to_add = set()
    values_to_remove = set()
    for element in elements:
        if isinstance(element, tuple):
            match element[0]:
                case 'sus':  # non-chord tone -> tendency tones
                    handle_sus(element[1], root_value, values_to_add, values_to_remove)
                case 'add':  # added tone
                    handle_add(element[1], root_value, values_to_add)
                case 'no':  # omission
                    handle_omission(element[1], root_value, values_to_remove)
                case 'set':
                    for set_element in element[1]:
                        if set_element.startswith("no"):
                            handle_omission(set_element[2], root_value, values_to_remove)
                        else:
                            handle_set_pitch_number(root_value, set_element, values_to_add)
                case 'M':
                    handle_major(element[1], root_value, values_to_add)
                case 'number':
                    handle_number(element[1], root_value, values_to_add, values_to_remove)
                case 'pitch_number':
                    handle_pitch_number(element[1], root_value, values_to_add, values_to_remove)
                case _:
                    raise ValueError(f"Type of element not found '{element[0]}'.")
        elif isinstance(element, str):
            match element[0]:
                case '6/9':
                    # TODO: finish this one
                    pass
                case _:
                    raise ValueError("Type of element not found.")

    return values_to_add, values_to_remove


def handle_pitch_number(element, root_value, values_to_add, values_to_remove):
    if element.startswith("b"):
        number = element[1:]
        offset = -0.5
    elif element.startswith("#"):
        number = element[1:]
        offset = 0.5
    else:
        raise ValueError(f"Unknown type inside set '{element}'.")
    match number:
        case '5':
            values_to_add.add(root_value + 7 * 0.5 + offset)
            values_to_remove.add(root_value + 7 * 0.5)
        case '9':
            values_to_add.add(root_value + 14 * 0.5 + offset)
        case '11':
            values_to_add.add(root_value + 17 * 0.5 + offset)
        case _:
            raise ValueError(f"Unknown pitch number '{number}'.")


def handle_major(element, root_value, values_to_add):
    match element:
        case '7':
            values_to_add.add(root_value + 11 * 0.5)
        case '9':
            values_to_add.update([root_value + 11 * 0.5, root_value + 14 * 0.5])
        case '11':
            values_to_add.update([root_value + 11 * 0.5, root_value + 14 * 0.5, root_value + 17 * 0.5])
        case '13':
            values_to_add.update([root_value + 11 * 0.5, root_value + 14 * 0.5, root_value + 17 * 0.5,
                                  root_value + 21 * 0.5])
        case _:
            raise ValueError(f"Type of Major not found '{element}'.")


def handle_number(element, root_value, values_to_add, values_to_remove):
    match element:
        case '2':
            values_to_add.add(root_value + 2 * 0.5)
        case '5':
            major_third = root_value + 4 * 0.5
            minor_third = root_value + 3 * 0.5
            values_to_remove.update([major_third, minor_third])
            perfect_fifth = root_value + 7 * 0.5
            values_to_add.add(perfect_fifth)
        case '6':
            values_to_add.add(root_value + 9 * 0.5)
        case '7':
            values_to_add.add(root_value + 10 * 0.5)
        case '9':
            values_to_add.update([root_value + 10 * 0.5, root_value + 14 * 0.5])
        case '11':
            values_to_add.update([root_value + 10 * 0.5, root_value + 14 * 0.5, root_value + 17 * 0.5])
        case '13':
            values_to_add.update([root_value + 10 * 0.5, root_value + 14 * 0.5, root_value + 17 * 0.5,
                                  root_value + 21 * 0.5])
        case _:
            raise ValueError(f"Invalid chord number '{element}'.")


def handle_set_pitch_number(root_value, element, values_to_add):
    if element.startswith("b"):
        number = element[1:]
        handle_add(number, root_value - 0.5, values_to_add)
    elif element.startswith("#"):
        number = element[1:]
        handle_add(number, root_value + 0.5, values_to_add)
    elif element.isdigit():
        number = element
        handle_add(number, root_value, values_to_add)
    else:
        raise ValueError(f"Unknown type inside set '{element}'.")


def handle_sus(number, root_value, values_to_add, values_to_remove):
    major_third = root_value + 4 * 0.5
    minor_third = root_value + 3 * 0.5
    values_to_remove.update([major_third, minor_third])
    match number:
        case '2':
            major_second = root_value + 2 * 0.5
            values_to_add.add(major_second)
        case 'b2':
            flattened_second = root_value + 2 * 0.5 - 0.5
            values_to_add.add(flattened_second)
        case '4':
            perfect_fourth = root_value + 5 * 0.5
            values_to_add.add(perfect_fourth)
        case '#4':
            tritone = root_value + 5 * 0.5 + 0.5
            values_to_add.add(tritone)
        case _:
            raise ValueError(f"Type of sus chord not found '{number}'.")


def handle_add(number, root_value, values_to_add):
    match number:
        case '2':
            values_to_add.add(root_value + 2 * 0.5)
        case '4':
            values_to_add.add(root_value + 5 * 0.5)
        case '5':
            values_to_add.add(root_value + 7 * 0.5)
        case '6':
            values_to_add.add(root_value + 9 * 0.5)
        case '9':
            values_to_add.add(root_value + 14 * 0.5)
        case '11':
            values_to_add.add(root_value + 17 * 0.5)
        case '13':
            values_to_add.add(root_value + 21 * 0.5)
        case _:
            raise ValueError(f"Unknown 'add' value '{number}'.")


def handle_omission(number, root_value, values_to_remove):
    match number:
        case '3':
            major_third = root_value + 4 * 0.5
            minor_third = root_value + 3 * 0.5
            values_to_remove.update([major_third, minor_third])
        case '5':
            values_to_remove.add(root_value + 7 * 0.5)
        case _:
            raise ValueError(f"Type of omission not found '{number}'.")


def get_notes_from_inversion(root_value, inversion, result_set):

    if len(inversion[1]) == 1:
        note_value = roots[inversion[1][0]]
    else:
        note_value = roots[inversion[1][0]] + get_pitch_value(inversion[1][1])

    if note_value == root_value:
        return result_set

    # a chord is in root position if its root is the lowest note
    if note_value < root_value:
        raise ValueError(f"Note value '{note_value}' < Root value '{root_value}'.")

    if note_value in result_set:
        result_set.remove(note_value)
        result_set.add(note_value - 12 * 0.5)
    else:
        raise ValueError("Note not found in chord.")

    return result_set


def get_scale(root_value, result_set):
    aux_set = set([element % 6 for element in result_set])
    for key, value in scale_templates.items():
        normalized_scale = set([(element + root_value) % 6 for element in value])
        if aux_set.issubset(normalized_scale):
            if DEBUG:
                print(f"Transposed scale: {normalized_scale}; Result set: {result_set}")
            return key, set([element + root_value for element in value])
    return None


def get_note_names_from_scale(scale, root_value, root_note, pitch):
    value_to_note = {}
    used_roots = {'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'A': 0, 'B': 0}

    scale.remove(root_value)
    used_roots[root_note] += 1
    value_to_note[root_value] = root_note + pitch if pitch is not None else root_note

    for note_value in scale:
        note_value_normalized = note_value % 6
        note = notes.get(note_value_normalized)
        if isinstance(note, list):
            if used_roots[note[0][0]] == 0:
                used_roots[note[0][0]] += 1
                value_to_note[note_value_normalized] = note[0]
            elif used_roots[note[1][0]] == 0:
                used_roots[note[1][0]] += 1
                value_to_note[note_value_normalized] = note[1]
            else:
                value_to_note[note_value_normalized] = note[0]  # there has to be a root note repetition in this case
        elif isinstance(note, str):
            next_note = (note_value_normalized + 0.5) % 6
            prev_note = (note_value_normalized - 0.5) % 6
            found = False
            match note:
                case "E":  # <=> Fb
                    if root_value != note_value_normalized and prev_note in scale and used_roots["F"] == 0:
                        used_roots["F"] += 1
                        value_to_note[note_value_normalized] = "Fb"
                        found = True
                case "F":  # <=> E#
                    if root_value != note_value_normalized and next_note in scale and used_roots["E"] == 0:
                        used_roots["E"] += 1
                        value_to_note[note_value_normalized] = "E#"
                        found = True
                case "B":  # <=> Cb
                    if root_value != note_value_normalized and prev_note in scale and used_roots["C"] == 0:
                        used_roots["C"] += 1
                        value_to_note[note_value_normalized] = "Cb"
                        found = True
                case "C":  # <=> B#
                    if root_value != note_value_normalized and next_note in scale and used_roots["C"] == 0:
                        used_roots["B"] += 1
                        value_to_note[note_value_normalized] = "B#"
                        found = True
            if not found:
                if used_roots[note] == 0:
                    value_to_note[note_value_normalized] = note
                    used_roots[note[0]] += 1
                else:
                    if DEBUG:
                        print(f"Root already used! '{note}'")
                    value_to_note[note_value_normalized] = note
                    used_roots[note[0]] += 1
        else:
            raise TypeError(f"Unknown type.")

    return value_to_note


def get_note_names_from_chord(values, value_to_note):
    aux = []
    for value in values:
        if value < 0:
            priority = -((value * -1) // 6)
        else:
            priority = value // 6

        normalized_value = value % 6
        if normalized_value not in value_to_note:
            raise Exception(f"{normalized_value} not in value_to_note")

        note = value_to_note[normalized_value]
        priority += value / 6
        aux.append((priority, note))

    aux.sort(key=lambda x: x[0])
    return [note for _, note in aux]  # return as list to preserve order


def get_notes(chord):
    root = chord[0]
    pitch = chord[1]
    quality = chord[2]
    elements = chord[3]
    inversion = chord[4]

    # root
    result_set = set()
    root_value = roots[root] + get_pitch_value(pitch)
    result_set.add(root_value)

    # quality
    result_set.update(get_notes_from_quality(root_value, quality))

    # elements
    values_to_add, values_to_remove = get_notes_from_elements(root_value, elements)
    has_common_elements = bool(values_to_add & values_to_remove)
    if has_common_elements:
        raise ValueError("Chord name is not constructed properly.")

    result_set.difference_update(values_to_remove)
    result_set.update(values_to_add)

    # inversion
    if inversion is not None:
        result_set = get_notes_from_inversion(root_value, inversion, result_set)

    # get scale
    scale = get_scale(root_value, result_set)
    if scale is None:
        raise Exception("Scale not found")

    if DEBUG:
        print(f"Scale: {scale[0]} - {scale[1]}")

    # get note names from scale (choose flat or sharp, etc.)
    value_to_note = get_note_names_from_scale(scale[1], root_value, root, pitch)
    print(f"Scale: {scale[0]} - {value_to_note.values()}")

    # get names of the notes in the chord
    chord_notes = get_note_names_from_chord(result_set, value_to_note)
    return chord_notes


def main():
    try:
        chord = input("Write a chord: ")
    except KeyboardInterrupt as e:
        print(e)
        return

    try:
        parsed_chord = parser.parse(chord)
        if DEBUG:
            print(f"After parsing: {parsed_chord}")
    except Exception as e:
        print("Error: ", e)
        if DEBUG:
            traceback.print_exc()
        return

    try:
        chord_notes = get_notes(parsed_chord)
        print(f"Chord notes (lowest to highest): {chord_notes}")
    except Exception as e:
        print("Error: ", e)
        if DEBUG:
            traceback.print_exc()
        return


if __name__ == "__main__":
    main()
