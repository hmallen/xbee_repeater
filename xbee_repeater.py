import logging
import serial
import time

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

serial_device = '/dev/ttyUSB0'
serial_baudrate = 19200


if __name__ == '__main__':
    ser = serial.Serial(
        port=serial_device,
        baudrate=serial_baudrate,
        timeout=1
    )

    if ser.in_waiting > 0:
        logger.debug('Flushing serial buffer.')
        while ser.in_waiting > 0:
            flush_char = ser.read()
            logger.debug('flush_char: ' + str(flush_char))

    logger.info('Repeater ready for incoming messages.')
    while True:
        try:
            if ser.in_waiting > 0:
                incoming_char = ser.read()
                logger.debug('incoming_char: ' + str(incoming_char))
                if incoming_char == b'H' or incoming_char == b'M':
                    bytes_written = ser.write(incoming_char)
                    logger.debug('bytes_written: ' + str(bytes_written))

            time.sleep(0.001)

        except Exception as e:
            logger.exception(e)

        except KeyboardInterrupt:
            break
