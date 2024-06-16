import re


def markdown_to_blocks(markdown):
    markdown_blocks = []
    block_queue = []

    for i, blocks in enumerate(markdown.split("```")):
        if i % 2 == 0:
            for block in blocks.split("\n"):
                striped_block = block.strip()
                if striped_block != "":
                    block_queue.append(striped_block)
                else:
                    if len(block_queue) > 0:
                        markdown_blocks.append("\n".join(block_queue))
                    block_queue.clear()   

            if len(block_queue) > 0:
                markdown_blocks.append("\n".join(block_queue))
                block_queue.clear()
        else:
            markdown_blocks.append(f"```\n{blocks.strip()}\n```")

    return markdown_blocks
