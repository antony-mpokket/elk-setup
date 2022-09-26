from importlib.resources import Package
import ElkJsonFormatter as ElkJsonFormatter

package_name = __file__.split('\\')[-2]
elkJsonFormatter = ElkJsonFormatter.ElkJsonFormatter(package_name)
logger = elkJsonFormatter.get_logger()


def process(msg):
    logger.info("Before the process")
    print(msg)
    logger.info("After the process")


process("Test logging")