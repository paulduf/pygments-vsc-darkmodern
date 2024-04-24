from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Keyword,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
)


class DarkModern(Style):
    """VSCode Default Dark Modern"""

    styles = {
        Number:                 '#b6cea9',
        Operator:               '#d4d4d4',
        Comment:                '#6d9957', # this is a commment
        Keyword.Namespace:      '#c287a0',
        Keyword.Reserved:       '#c287a0',
        Keyword.Type:           '#61c8b0',
        Keyword:                '#639bd4',
        Name:                   '#7fd0fd',
        Name.Class:             '#61c8b0',
        Name.Namespace:         '#61c8b0',
        Error:                  '#61c8b0',
        Name.Function:          '#dbdcac',
        String:                 '#c9937a',
        Punctuation:            '#f9c922'
    }
