import ElkJsonFormatter

elkJsonFormatter = ElkJsonFormatter.ElkJsonFormatter()
logger = elkJsonFormatter.get_logger()


def process(msg):
    logger.info("Before the process")
    print(msg)
    logger.info("After the process")


process("Test logging")